from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    # path('login/', views.user_login, name = 'user_login'),
    path('login/', views.LoginView.as_view(), name = 'user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'user_logout'),
    path('signup/',views.user_signup, name = 'user_signup'),
    path('activate/<uidb64>/<token>/', views.activate_user, name='activate'),
    path('change-password/', views.PasswordChangeView.as_view(), name='change_password'),
    
    path(
        'change-password-mail-sent/',
        auth_views.PasswordResetDoneView.as_view(
            template_name = 'users/password/password_reset_mail_sent_notification.html'
        ),
        name = 'change_password_mail_sent'
    ), 
    
    path(
        'confirm-password-reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name = 'users/password/password_reset_confirmation.html'    
        ),
        name = 'confirm_password_reset'
    ),
    
    path(
        'password-reset-completed/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name = 'users/password/password_reset_complete.html'
        ),
        name = 'password_reset_complete'
    ),
]
