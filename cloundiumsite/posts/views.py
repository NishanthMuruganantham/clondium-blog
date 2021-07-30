from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostCreationForm


def home(request):
    return render(request, 'posts/post_detail.html')



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