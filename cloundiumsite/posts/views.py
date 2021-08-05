from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from .models import Post
from .forms import PostCreationForm, CommentForm
from django.template.loader import render_to_string
from django.http import JsonResponse

def home(request):
    return render(request, 'posts/post_detail.html')



class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = 'posts/post_list.html'
    
    total_data = Post.objects.count()
    data = Post.objects.all().order_by('-id')[:3]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_data'] = self.total_data
        context['data'] = self.data
        return context
        


def post_list(request):
    total_data = Post.objects.count()
    data = Post.objects.all().order_by('-id')[:3]
    return render(request, 'posts/post_list.html',{'data':data,'total_data':total_data})



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
    form = CommentForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm(instance=self.request.user)
        return context
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        blog_post = self.get_object()
        form.instance.commenter = request.user
        form.instance.post = blog_post
        print('wcwedfcame')
        form.save()
        return redirect(reverse('posts:post_detail',kwargs={'pk':blog_post.pk,'slug':blog_post.slug}))



class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    form_class = PostCreationForm
    
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


# Load More
def load_more_data(request):
	offset=int(request.GET['offset'])

	limit=int(request.GET['limit'])
	data=Post.objects.all().order_by('-pk')[offset:offset+limit]
	t=render_to_string('posts/sample.html',{'data':data})
	return JsonResponse({'data':t}
)