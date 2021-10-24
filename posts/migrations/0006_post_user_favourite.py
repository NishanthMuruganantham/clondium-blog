# Generated by Django 3.2.4 on 2021-08-09 17:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_comment_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_favourite',
            field=models.ManyToManyField(blank=True, related_name='favourite_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]