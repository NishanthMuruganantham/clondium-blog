# Generated by Django 3.2.4 on 2021-08-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_alter_post_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True),
        ),
    ]