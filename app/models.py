from django.db import models
from django.core.validators import (
    EmailValidator
)


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
    

class PatientDetails(models.Model):
    GENDERS = (
        ('M','MALE'),
        ('F','FEMALE'),
        ('O','OTHERS')
    )
    Name = models.CharField(max_length=256)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=2,choices=GENDERS)
    Disease = models.TextField()
    Contact = models.IntegerField()
    Hospital = models.ForeignKey('DetailsOfDoctors',on_delete=models.CASCADE)
    def __str__(self):
        return self.Name
    