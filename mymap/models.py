from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Destination(models.Model):
    user = models.ForeignKey(User)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    month_visited = models.DateField
    year_visited = models.DateField
    month_to-visit = models.DateField
    year_to_visit = models.DateField
    my_experience = models.BooleanField
    destination_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-created_on']

    def _str_(self):
        return self.title


class Food(models.Model):
    destination = models.ForeignKey(Destination)
    name_of_food = models.CharField(max_length=200)
    food_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-created_on']

    def _str_(self):
        return self.title
