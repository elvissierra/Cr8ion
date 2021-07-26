from django.db import models
from django.contrib.auth.models import User

class Prints(models.Model):
    title = models.CharField(max_length=30)
    creator = models.CharField(max_length=30)
    stl = models.FileField(upload_to= 'storage/stls/')
    cover = models.ImageField(upload_to= 'storage/covers/')

    def __str__(self):
        return self.name

