# Generated by Django 3.2.4 on 2021-08-19 09:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210803_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
