from django.db import models
from django.core.validators import (
    EmailValidator
)

# Create your models here.
class DetailsOfDoctors(models.Model):
    name = models.CharField(max_length = 256)
    address = models.TextField()
    city = models.CharField(max_length = 256)
    state = models.CharField(max_length = 256)
    email = models.CharField(max_length = 256,validators=[EmailValidator('The Entered Email is not valid.')])
    number = models.IntegerField(null=True)
    image = models.ImageField()
    def __str__(self):
        return self.name
    