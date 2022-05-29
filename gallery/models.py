from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
        
        
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=None)
    category = models.ManyToManyField(Category)
    post_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-post_time']

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id__icontains=id)
        return image

    @classmethod
    def get_image_by_category(cls, category):
        image = cls.objects.filter(category__icontains=category)
        return image

    @classmethod
    def get_image_by_location(cls, location):
        image = cls.objects.filter(location__icontains=location)
        return image

    @classmethod
    def search_by_name(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images