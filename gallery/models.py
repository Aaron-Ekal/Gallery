from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=30)
    description = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)
    
    
class Location(models.Model):
    name = models.CharField(max_length=30)