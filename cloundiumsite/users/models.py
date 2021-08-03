from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class AccountManager(BaseUserManager):
    
    def create_user(self, email, username, password):
        if not email:
            raise ValueError('Email is mandatory')
        if not username:
            raise ValueError('Username is mandatory')
        user = self.model(email = self.normalize_email(email), username = username)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    
    def create_superuser(self, email, username, password):
        if not email:
            raise ValueError('Email is mandatory')
        if not username:
            raise ValueError('Username is mandatory')
        user = self.model(email = self.normalize_email(email), username = username)
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class UserAccount(AbstractUser):
    email           = models.EmailField(verbose_name = 'email', max_length = 60, unique = True)
    username        = models.CharField(max_length = 30, unique = True)
    date_joined     = models.DateTimeField(auto_now_add = True)
    last_login      = models.DateTimeField(auto_now_add = True)
    is_admin        = models.BooleanField(default = False)
    is_staff        = models.BooleanField(default = False)
    is_active       = models.BooleanField(default = False)
    is_superuser    = models.BooleanField(default = False)
    profile_picture = models.ImageField(upload_to = "accounts/images/profile_pictures", default = "accounts/images/default/Default_Profile_picture.png", null = True, blank = True)
    hide_email      = models.BooleanField(default = True)
    first_name      = models.CharField(max_length = 30, null = True, blank = True)
    last_name       = models.CharField(max_length = 30, null = True, blank = True)
    
    bio             = models.TextField(max_length = 255, blank = True, null = True)
    date_of_birth   = models.DateField(blank = True, null = True)
    website         = models.URLField(blank = True, null = True)
    
    facebook        = models.URLField(blank = True, null = True)
    instagram       = models.URLField(blank = True, null = True)
    twitter         = models.URLField(blank = True, null = True)
    google_plus     = models.URLField(blank = True, null = True)
    linkedin        = models.URLField(blank = True, null = True)
    github          = models.URLField(blank = True, null = True)
    
    objects = AccountManager()
    
    USERNAME_FIELD  = "email"
    REQUIRED_FIELDS = ["username",]
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj = None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    class Meta:
        verbose_name_plural = 'User Accounts'