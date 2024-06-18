from django.db import models
from django.contrib.auth.models import User


class Print(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    stl = models.FileField(upload_to="store/stls/")
    cover = models.ImageField(upload_to="store/covers/", null=True, blank=True)

    def __str__(self):
        return self.title

    def num_likes(self):
        return self.liked.all().count()

#to be refactored

class Likes(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name="like")
    print = models.ForeignKey(Print, on_delete=models.SET_NULL, null=True)
    likes_count = models.BigIntegerField(default=0)
    comments = models.CharField(max_length=50)
