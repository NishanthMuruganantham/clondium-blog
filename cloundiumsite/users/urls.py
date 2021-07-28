from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    # path('login/', views.user_login, name = 'user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'user_logout'),
    path('signup/',views.user_signup, name = 'user_signup'),
    path('activate/<uidb64>/<token>', views.activate_user, name='activate'),
    path('login/', views.LoginView.as_view(), name = 'user_login'),
]
