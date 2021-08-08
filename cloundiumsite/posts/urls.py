from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'posts'

urlpatterns = [
    path('load-more-data',views.load_more_data,name='load_more_data'),
    path('load-more-comments',views.load_more_comments,name='load_more_comments'),
    path('',views.PostListView.as_view(), name='home'),
    path('posts/new', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<pk>/<slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<pk>/<slug>/edit', views.PostUpdateView.as_view(), name='post_update'),
    path('post-like/',views.post_like_view, name='post_like'),
    path('comment-like/',views.comment_like_view, name='comment_like'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

