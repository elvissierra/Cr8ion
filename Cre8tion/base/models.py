from os import makedirs
from django.db import models


#user = models.ForeignKey(
#User, on_delete=models.CASCADE, null=True, blank=True)

class Prints (models.Model):

    filename = models.CharField(max_length=30)
    creator = models.CharField(max_length=30)
    stl = models.FileField(upload_to= "media")
    cover = models.ImageField(upload_to= "media")
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename

    def delete(self, *args, **kwargs):
        self.stl.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

#class upload(models.Model):
#    title= models.CharField(max_length= 50)
#    upload= models.FileField(upload_to= "media")

