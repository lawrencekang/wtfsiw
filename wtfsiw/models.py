from django.db import models

# user model

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    locations_visited = models.CommaSeparatedIntegerField(max_length=500)
    home_address = models.CharField(max_length=200, null=True)
    home_location = models.CharField(max_length=200, null=True)

    def __str__(self):             
        return ('%s %s') %(self.first_name, self.last_name)

class Location(models.Model):
    user = models.ManyToManyField(User)
    business_name = models.CharField(max_length=200)
    address = models.CharField(max_length = 200)
    location = models.CharField('GPS coordinates', max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):             
        return ('%s %s') %(self.business_name, self.address)
