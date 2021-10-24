# Generated by Django 3.2.4 on 2021-08-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.TextField(default='This is the description for the post which were created before this field was included. The minimun length is 250 characters and maximum klength is 300 characters so one can get the full description for this post', max_length=300),
        ),
    ]