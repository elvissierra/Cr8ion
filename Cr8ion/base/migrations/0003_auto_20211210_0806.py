# Generated by Django 3.2.9 on 2021-12-10 14:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_auto_20211122_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='print',
            name='dislikes',
        ),
        migrations.AddField(
            model_name='print',
            name='likes_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='print',
            name='likes',
            field=models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
