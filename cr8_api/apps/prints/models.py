from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.contenttypes.models import ContentType

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