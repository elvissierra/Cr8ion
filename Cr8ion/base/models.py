from django.db import models
from django.contrib.auth.models import User


class Print(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    stl = models.FileField(upload_to="store/stls/")
    cover = models.ImageField(upload_to="store/covers/", null=True, blank=True)
    likes = models.ManyToManyField(User, related_name="like")
    likes_count = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title
