from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    year = models.IntegerField(blank=True, null=True)  # Allowing NULL values
    img = models.ImageField(upload_to='images/',  default='default_image.jpg')

    def __str__(self):
        return self.name
