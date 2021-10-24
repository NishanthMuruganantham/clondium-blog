from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import readtime
from taggit.managers import TaggableManager
from django.core.validators import MinLengthValidator


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length = 40)
    slug = models.SlugField(allow_unicode = True, unique = True, blank = True, null = True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('posts:home')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    author              = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts')
    title               = models.CharField(max_length = 100)
    short_description   = models.TextField(max_length=300,validators=[MinLengthValidator(4)])
    content             = RichTextField(blank = True, null = True)
    created_time        = models.DateTimeField(auto_now_add = True)
    header_image        = models.ImageField(blank = True, null = True, upload_to='posts/images/')
    slug                = models.SlugField(allow_unicode = True, unique = False)
    category            = models.ForeignKey(Category, on_delete = models.CASCADE, default=1, related_name='posts')
    likes               = models.ManyToManyField(User,related_name='post')
    user_favourite      = models.ManyToManyField(User, related_name='favourite_posts', blank = True)
    tags                = TaggableManager()
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('posts:post_detail',kwargs = {'pk':self.pk, 'slug':self.slug})
    
    def get_readtime(self):
        result = readtime.of_html(self.content)
        return result.text
    
    def number_of_likes(self):
        return self.likes.count()
    
    def number_of_saves(self):
        return self.user_favourite.count()



class Comment(models.Model):
    post            = models.ForeignKey(Post, on_delete=models.CASCADE,  related_name='comments')
    commenter       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content         = models.TextField()
    commented_at    = models.DateTimeField(auto_now_add=True)
    likes           = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    dislikes        = models.ManyToManyField(User, related_name='comment_dislikes', blank=True)
    
    def __str__(self):
        return self.content
    
    def number_of_likes(self):
        return self.likes.count()
    
    def number_of_dislikes(self):
        return self.dislikes.count()



class Reply(models.Model):
    comment         = models.ForeignKey(Comment, on_delete=models.CASCADE,  related_name='replies')
    replier         = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    content         = models.TextField()
    replied_at      = models.DateTimeField(auto_now_add=True)
    likes           = models.ManyToManyField(User, related_name='reply_likes', blank=True)
    dislikes        = models.ManyToManyField(User, related_name='reply_dislikes', blank=True)
    
    def __str__(self):
        return self.content
    
    def number_of_likes(self):
        return self.likes.count()
    
    def number_of_dislikes(self):
        return self.dislikes.count()