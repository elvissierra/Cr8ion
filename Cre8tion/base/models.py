from django.db import models
from django.contrib.auth.models import User
from django.utils import tree

# from django.contrib.auth.models import User


class Print(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    stl = models.FileField(upload_to="store/stls/")
    cover = models.ImageField(upload_to="store/covers/", null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name="like")
    dislikes = models.ManyToManyField(User, blank=True, related_name="dislike")
    like_count = models.BigIntegerField(default="0")

    def __str__(self):
        return self.title


# class Post(models.Model):
#    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#    comment = models.TextField()
#    likes = models.ManyToManyField(User, blank=True, null=True, related_name="like")
#    dislikes = models.ManyToManyField(User, blank= True, null= True, related_name= "dislike")
#    like_count = models.BigIntegerField(default="0")
