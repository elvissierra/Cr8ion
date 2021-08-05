from django.db import models


#user = models.ForeignKey(
#User, on_delete=models.CASCADE, null=True, blank=True)

class Prints (models.Model):
    filename = models.CharField(max_length=50)
    creator = models.CharField(max_length=50)
    created= models.DateTimeField(auto_now_add=True)
    stl = models.FileField(upload_to= 'media/stls')
    cover = models.ImageField(upload_to= 'media/covers/')
    

    def __str__(self):
        return self.filename

    def delete(self, *args, **kwargs):
        self.stl.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)



