from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model, authenticate
from django.forms import widgets

User = get_user_model()



class SignupForm(UserCreationForm):
    
    password1 = forms.CharField(label = "Password", widget = forms.PasswordInput(
        attrs = {'class': 'input100'}
    ))
    
    password2 = forms.CharField(label = "Confirm Password", widget = forms.PasswordInput(
        attrs = {'class': 'input100'}
    ))
    
    class Meta:
        model = User
        fields = ('email','username','password1','password2')
        
        widgets = {
            'username': forms.TextInput(
                attrs={'class':'input100'}
            ),
            'email': forms.EmailInput(
                attrs={'class':'input100'}
            ),
            'password1': forms.PasswordInput(
                attrs={'class':'input100'}
            ),
            'password2': forms.PasswordInput(
                attrs={'class':'input100'}
            )
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




class LoginForm(AuthenticationForm):
    
    
    username = forms.CharField(
        label = "username",
        widget = forms.EmailInput(
            
            attrs = {
                'class': 'input100'
            }
        )
    )
    
    password = forms.CharField(
        label = "password",
        widget = forms.PasswordInput(
            attrs = {
                'class': 'input100'
            }
        )
    )
    
    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = 'username or passoword is invalid'
        super().__init__(*args, **kwargs)
    
    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')

    #     if username is not None and password:
    #         self.user_cache = authenticate(self.request, username=username, password=password)
    #         if self.user_cache is None:
    #             try:
    #                 user_temp = User.objects.get(email=username)
    #                 print(user_temp)
    #             except:
    #                 user_temp = None

    #             if user_temp is not None:
    #                     self.confirm_login_allowed(user_temp)
    #             else:
    #                 raise forms.ValidationError(
    #                     self.error_messages['invalid_login'],
    #                     code='invalid_login',
    #                     params={'username': self.username_field.verbose_name},
    #                 )

    #     return self.cleaned_data



class ProfileEditForm(UserChangeForm):
    profile_picture = forms.ImageField(label=('profile_picture'),error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    class Meta:
        fields = ('username','first_name','last_name','email','profile_picture')
        model = User
        
        widgets = {
            'username': forms.TextInput(
                attrs = {'class': 'form-control'}
            ),
            'first_name' : forms.TextInput(
                attrs = {'class': 'form-control'}
            ),
            'last_name' : forms.TextInput(
                attrs = {'class': 'form-control'}
            ),
            'email' : forms.TextInput(
                attrs = {'class': 'form-control'}
            ),
            # 'date_joined' : forms.TextInput(
            #     attrs = {'class': 'form-control'}
            # )
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].disabled = True
        