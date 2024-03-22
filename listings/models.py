from django.db import models
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}, {self.contact}"

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Rules_Terms(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

# class Images(models.Model):
#     photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
#     photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     def __str__(self):
#         return self.photo_main

class Address(models.Model):
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)  # or province
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    address_map_link = models.CharField()
    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state}, {self.postal_code}, {self.country}"

class Listing(models.Model):
    title = models.CharField(max_length=200)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    monthly_rent = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sqft = models.IntegerField()
    description = models.TextField(blank=True)
    rules_and_terms = models.ManyToManyField(Rules_Terms, blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    contact = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_available = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title





# Address Map Link **
# Apartment Availability
# Move in Cost:
#     First Monthly
#     Security Deposit
#     Broker Fee
#     Total Cost (First Month + Security Deposit + Broker Fee)
#for sale / for rent