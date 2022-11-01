from django.db import models

# Create your models here.
class MyImage(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=500)
    def __str__(self):
        return self.title
    @property
    def image_get(self):
        return self.image.url