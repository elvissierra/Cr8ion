from django.db import models
from django.contrib.auth.models import User
import uuid

def default_user():
    user, created = User.objects.get_or_create(
        username = "default user",
        defaults = {"email" : "default@gmail.com"}
    )
    return user

class Print(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=default_user)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=50, default="empty")
    created = models.DateTimeField(auto_now_add=True)
    stl = models.FileField(upload_to="store/stls/")
    cover = models.ImageField(upload_to="store/covers/", null=True, blank=True)

    def __str__(self):
        return self.title

    def num_likes(self):
        return self.liked.all().count()