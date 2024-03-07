from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length = 50)
    rating = models.IntegerField(
        validators = [MaxValueValidator(5), MinValueValidator(1)])
    author = models.CharField(null = True ,  max_length=50)
    is_bestselling = models.BooleanField(default = False)
    slug = models.SlugField(default="",null=False)
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f"{self.title} (Rating: {self.rating})"
    