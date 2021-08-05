from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'posts'

urlpatterns = [
    path('load-more-data',views.load_more_data,name='load_more_data'),
    path('',views.PostListView.as_view(), name='home'),
    path('posts/new', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<pk>/<slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<pk>/<slug>/edit', views.PostUpdateView.as_view(), name='post_update'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

