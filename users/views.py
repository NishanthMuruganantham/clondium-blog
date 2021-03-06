from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth import get_user_model
from django.views import View, generic
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordResetForm

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, SignupForm, ProfileEditForm
from .tokens import account_activation_token
from posts.models import Post


User = get_user_model()


#* FOR SENDING ACTIVATION EMAIL TO THE SIGNUP USER
def send_activation_email(request, user, user_email):
    current_site = get_current_site(request)
    mail_subject = "Activate your account"
    message = render_to_string(
        'users/account_activation_email.html', {
            'user'  : user,
            'domain': current_site.domain,
            'uid'   : urlsafe_base64_encode(force_bytes(user.pk)),
            'token' : account_activation_token.make_token(user),
        }
    )
    to_email = user_email
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()


#* TO ACTIVATE THE USER
def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'users/user_activation_link_success.html')
    else:
        return HttpResponse('Activation link is invalid!')


#* FOR SENDING PASSWORD RESET MAIL TO THE USER
def send_password_reset_mail(request, user, user_email):
    current_site = get_current_site(request)
    mail_subject = f"Reset Your Password for {current_site}"
    message = render_to_string(
        'users/password/password_reset_link_email.html',{
            'user'  : user,
            'domain': current_site.domain,
            'uid'   : urlsafe_base64_encode(force_bytes(user.id)),
            'token' : default_token_generator.make_token(user),
        }
    )
    to_email = user_email
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()


#* CUSTOM LOGIN VIEW
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect(reverse('posts:home')) 
                else:
                    messages.error(request,'Please click the link in the activation mail sent to your registered mail id to activate your account')
                    return redirect(reverse('posts:home'))
            else:
                messages.error(request,'username or password not correct')
                return redirect(reverse('posts:home'))
        else:
            return HttpResponse('login failed')
    else:
        form = LoginForm()
    return render(request,'users/login.html',{'form':form})


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'


#* SIGNUP WITH EMAIL AUTHENTICATION
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_active = False
            user.save()
            to_email = form.cleaned_data.get('email')
            send_activation_email(request = request, user = user,user_email = to_email)
            return render(request, 'users/send_user_activation_link.html')
    else:
        form = SignupForm()
    return render(request, 'users/registration.html', {'form': form})


class PasswordChangeView(View):
    template_name = 'users/password/password_reset.html'
    form_class = PasswordResetForm
    
    def post(self, request):
        password_reset_form = self.form_class(request.POST)
        if password_reset_form.is_valid():
            email_data = password_reset_form.cleaned_data['email']
            try:
                associated_user = User.objects.get(email__exact = email_data)
            except User.DoesNotExist:
                messages.error(request,'No user found for this email address')
                return render(request, self.template_name, {'form': password_reset_form})
            if associated_user:
                send_password_reset_mail(request,user = associated_user,user_email = email_data)
                return redirect(reverse('users:change_password_mail_sent'))
            else:
                messages.error(request,'No user found for this email address')
                return render(request, self.template_name, {'form': password_reset_form})
        return render(request, self.template_name, {'form': password_reset_form})
    
    
    def get(self, request):
        password_reset_form = PasswordResetForm()
        return render(request, self.template_name, {'form': password_reset_form})


class ProfileEditView(generic.UpdateView):
    model = User
    form_class = ProfileEditForm
    template_name = 'users/account_settings.html'
    success_url = reverse_lazy('users:account_settings')
    
    def get_object(self):
        return self.request.user



class UserPostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "users/user_about.html"
    ordering = ["-created_time"]
    
    def get_queryset(self):
        try:
            self.user = User.objects.get(username__exact = self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.user.posts.all().order_by("-created_time")
    
    def get_context_data(self, **kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        context['detailed_user'] = self.user
        return context



class UserSavedPostListView(LoginRequiredMixin, generic.ListView):
    login_url           = '/users/login/'
    redirect_field_name = "users:user_login"
    model               = Post
    context_object_name = "post_list"
    template_name       = "posts/post_list.html"
    ordering            = ["-created_time"]
    
    def get_queryset(self):
            return self.request.user.favourite_posts.all().order_by("-created_time")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_heading'] = "Saved Posts"
        return context



#* FOLLOW USER VIEW    
def follow_user(request):
    
    if request.POST.get('action') == 'post':
        followed_user_id = int(request.POST.get('followed_user_id'))
        #current_user_id     = int(request.POST.get('current_user_id'))
        print(followed_user_id)
        followed_user = get_object_or_404(User,id=followed_user_id)
        #current_user = get_object_or_404(User,current_user_id)
        print(followed_user)
        followed = False
        if followed_user_id != request.user.id:
            if followed_user.followers.filter(id = request.user.id):
                followed_user.followers.remove(request.user)
            else:
                followed_user.followers.add(request.user)
                followed = True
        
        followers_count = followed_user.followers.count()
        
        
        return JsonResponse(
            {
                'followers_count':followers_count,
                'followed':followed,
            }
        )