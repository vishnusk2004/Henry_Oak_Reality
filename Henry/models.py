from django.db import models


# Create your models here.
class Property(models.Model):
    title = models.TextField()
    location = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.IntegerField(null=True)
    parking_space = models.IntegerField(null=True)
    area = models.CharField(max_length=50)
    site_url = models.URLField(null=True, max_length=255)
    image_url = models.URLField(null=True, max_length=255)
    time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
