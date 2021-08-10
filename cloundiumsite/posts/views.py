from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Post, Comment
from .forms import PostCreationForm, CommentForm, ReplyForm
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from django.views import View

import json

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
        
        blog_post = get_object_or_404(Post,pk=self.kwargs['pk'])
        post_is_liked = False
        if blog_post.likes.filter(id = self.request.user.id).exists():
            post_is_liked = True
        print(post_is_liked)
        context['total_post_likes'] = blog_post.number_of_likes()
        context['post_is_liked'] = post_is_liked
        
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm(instance=self.request.user)
        return context
    
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        blog_post = self.get_object()
        form.instance.commenter = request.user
        form.instance.post = blog_post
        print('new comment added')
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




# Load More
def load_more_comments(request):
    print("called")
    post_id = int(request.GET['blog_post_id'])
    print(post_id)
    post = get_object_or_404(Post,pk=post_id)
    offset=int(request.GET['offset'])
    print(post)
    print(offset)
    limit=int(request.GET['limit'])
    data=post.comments.all().order_by('id')[offset:offset+limit]
    print(request.user.id)
    t=render_to_string('posts/sample2.html',{'data':data,'user':request.user})
    return JsonResponse({'data':t}
)


# #* POST LIKE VIEW    
def post_like_view(request):
    
    if request.POST.get('action') == 'post':
        result = ''
        id = int(request.POST.get('postid'))
        post = get_object_or_404(Post,id=id)
        liked = False
        
        if post.likes.filter(id = request.user.id).exists():
            post.likes.remove(request.user)
            result = post.number_of_likes()
        else:
            post.likes.add(request.user)
            result = post.number_of_likes()
            liked = True
        
        return JsonResponse({'result':result,'is_post_liked':liked})



#* COMMENT LIKE VIEW    
def comment_like_view(request):
    
    if request.POST.get('action') == 'post':
        id = int(request.POST.get('commentid'))
        comment = get_object_or_404(Comment,id = id)
        liked = False
        disliked = False
        
        if comment.likes.filter(id = request.user.id).exists():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
            liked = True
            if comment.dislikes.filter(id = request.user.id).exists():
                comment.dislikes.remove(request.user)
        
        likes_count = comment.number_of_likes()
        dislikes_count = comment.number_of_dislikes()
        
        return JsonResponse(
            {
                'likes_count':likes_count,
                'dislikes_count':dislikes_count,
                'is_comment_liked':liked,
                'is_comment_disliked':disliked
            }
        )


#* COMMENT DISLIKE VIEW    
def comment_dislike_view(request):
    
    if request.POST.get('action') == 'post':
        id = int(request.POST.get('commentid'))
        comment = get_object_or_404(Comment,id=id)
        liked = False
        disliked = False
        
        if comment.dislikes.filter(id = request.user.id).exists():
            comment.dislikes.remove(request.user)
        else:
            comment.dislikes.add(request.user)
            disliked = True
            if comment.likes.filter(id = request.user.id).exists():
                comment.likes.remove(request.user)
        
        likes_count = comment.number_of_likes()
        dislikes_count = comment.number_of_dislikes()
        
        return JsonResponse(
            {
                'likes_count':likes_count,
                'dislikes_count':dislikes_count,
                'is_comment_liked':liked,
                'is_comment_disliked':disliked,
            }
        )


#* ADD FAVOURITE POST VIEW
def add_to_favourites_post(request):
    if request.POST.get('action') == 'post':
        post_id = int(request.POST.get('post_id'))
        post = get_object_or_404(Post,id=post_id)
        favourite = False
        
        if post.user_favourite.filter(id = request.user.id).exists():
            post.user_favourite.remove(request.user)
        else:
            post.user_favourite.add(request.user)
            favourite = True
        
        return JsonResponse(
            {
                'is_favourite':favourite
            }
        )


class CommentReplyView(View):
    def post(self, request, post_pk, comment_pk, *args, **kwargs):
        blog_post = Post.objects.get(pk=post_pk)
        parent_comment = Comment.objects.get(pk=comment_pk)
        form = ReplyForm(request.POST)
        
        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.replier = request.user
            new_reply.comment = parent_comment
            new_reply.save()
        
        return redirect(reverse('posts:post_detail',kwargs={'pk':blog_post.pk,'slug':blog_post.slug}))