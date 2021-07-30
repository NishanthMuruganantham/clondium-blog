from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import readtime

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length = 40)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('posts:home')


class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts')
    title = models.CharField(max_length = 100)
    content = RichTextField(blank = True, null = True)
    created_time = models.DateTimeField(auto_now_add = True)
    header_image = models.ImageField(blank = True, null = True, upload_to='posts/images/')
    slug = models.SlugField(allow_unicode = True, unique = False)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default=1, related_name='posts')
    
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