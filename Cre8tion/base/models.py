from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# from django.contrib.auth.models import User

# user = models.ForeignKey(
# User, on_delete=models.CASCADE, null=True, blank=True)


class Print(models.Model):
    filename = models.CharField(max_length=50, default="")
    user = models.CharField(max_length=50, default="")
    description = models.TextField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    stl = models.FileField(upload_to="stls")
    cover = models.ImageField(upload_to="covers", null=True, blank=True)

    def __str__(self):
        return self.filename
