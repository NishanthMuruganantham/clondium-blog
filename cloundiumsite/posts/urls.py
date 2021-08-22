from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.PostListView.as_view(), name = 'home'),   #home view aka post list view
    path('posts/new', views.PostCreateView.as_view(), name = 'post_create'),    #create new post view
    path('posts/<pk>/<slug>/', views.PostDetailView.as_view(), name = 'post_detail'),   #post detail view
    path('posts/<pk>/<slug>/edit', views.PostUpdateView.as_view(), name = 'post_update'),   #post edit view
    path('posts/<pk>/<slug>/delete', views.PostDeleteView.as_view(), name = 'post_delete'), #post delete view
    path('load-more-comments', views.load_more_comments, name = 'load_more_comments'),  #load more comments view
    path('post-like/', views.post_like_view, name = 'post_like'),   #post like view
    path('add-to-favourite_posts', views.add_to_favourites_post, name = 'add_to_favourite_posts'),  #post save view
    path('posts/<int:post_pk>/comment/<int:comment_pk>/reply', views.CommentReplyView.as_view(), name = 'comment_reply'),   #comment reply view
    path('load-more-replies/', views.load_more_replies, name = 'load_more_replies'),    #load more reply view
    path('comment-like/', views.comment_like_view, name = 'comment_like'),  #comment like view
    path('comment-dislike/', views.comment_dislike_view, name = 'comment_dislike'), #comment dislike view
    path('reply-like/', views.reply_like_view, name = 'reply_like'),    #reply like view
    path('reply-dislike/', views.reply_dislike_view, name = 'reply_dislike'),   #reply dislike view
    path('posts/<int:post_pk>/<slug:post_slug>/comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name = "comment_delete"),   #comment delete view
    path('posts/<int:post_pk>/<slug:post_slug>/reply/<int:pk>/delete', views.ReplyDeleteView.as_view(), name = "reply_delete"), #reply delete view
    path('category/<category_slug>/posts/', views.CategoryPostListView.as_view(), name = "category_post_list"), #category wise post list view
    path('tag/<slug:slug>/', views.tagged, name = "tagged"),    #tag wise post list view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)