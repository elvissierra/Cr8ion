from django.db import models

#user = models.ForeignKey(
#User, on_delete=models.CASCADE, null=True, blank=True)

class Prints (models.Model):
    filename = models.CharField(max_length=50)
    creator = models.CharField(max_length=50)
    created= models.DateField(default= '')
    stl = models.FileField(upload_to= 'stls')
    cover = models.ImageField(upload_to= 'covers')
    

    def __str__(self):
        return self.filename

    def delete(self, *args, **kwargs):
        self.stl.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)



