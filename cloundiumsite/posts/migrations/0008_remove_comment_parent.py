# Generated by Django 3.2.4 on 2021-08-10 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]
