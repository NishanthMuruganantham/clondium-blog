from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'posts'

urlpatterns = [
    path('load-more-data', views.load_more_data, name = 'load_more_data'),
    path('load-more-comments', views.load_more_comments, name = 'load_more_comments'),
    path('',views.home, name = 'home'),
    path('posts/new', views.PostCreateView.as_view(), name = 'post_create'),
    path('posts/<pk>/<slug>/', views.PostDetailView.as_view(), name = 'post_detail'),
    path('posts/<pk>/<slug>/edit', views.PostUpdateView.as_view(), name = 'post_update'),
    path('post-like/', views.post_like_view, name = 'post_like'),
    path('comment-like/', views.comment_like_view, name = 'comment_like'),
    path('comment-dislike/', views.comment_dislike_view, name = 'comment_dislike'),
    path('reply-like/', views.reply_like_view, name = 'reply_like'),
    path('reply-dislike/', views.reply_dislike_view, name = 'reply_dislike'),
    path('add-to-favourite_posts', views.add_to_favourites_post, name = 'add_to_favourite_posts'),
    path('posts/<int:post_pk>/comment/<int:comment_pk>/reply', views.CommentReplyView.as_view(), name = 'comment_reply'),
    path('load-more-replies/', views.load_more_replies, name = 'load_more_replies'),
    path('tag/<slug:slug>/', views.tagged, name = "tagged"),
    path('category/<category_slug>/posts/', views.CategoryPostListView.as_view(), name = "category_post_list"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

