from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.contenttypes import fields
from django.contrib.contenttypes import models

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


class Likes(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    liked_object = fields.GenericForeignKey("object_type", "object_id")
    object_type = models.ForeignKey(models.ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()

    user_id = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["object_type", "object_id"], name="like_index_type_id"),
        ]
        constaints = [
            models.UniqueConstraint(
                fields=["object_type", "object_id", "user_id"],
                name="like_unique_type_id_user",                
            )
        ]
