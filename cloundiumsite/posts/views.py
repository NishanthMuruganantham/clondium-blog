from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from .models import Post
from .forms import PostCreationForm, CommentForm


def home(request):
    return render(request, 'posts/post_detail.html')



class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = 'posts/post_list.html'



class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    form_class = PostCreationForm
    
    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)



class PostDetailView(generic.DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm(instance=self.request.user)
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        blog_post = self.get_object()
        form.instance.commenter = request.user
        form.instance.post = blog_post
        return redirect(reverse('posts:post_detail',kwargs={'pk':blog_post.pk,'slug':blog_post.slug}))



class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    form_class = PostCreationForm
    
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)