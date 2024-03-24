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
    
class Move_In_Cost(models.Model):
    first_monthly = models.FloatField()
    security_diposit = models.FloatField()
    broker_fee = models.FloatField()
    def __str__(self):
        return f"{self.first_monthly}, {self.security_diposit}, {self.broker_fee}"
    
class Property_Status(models.Model):
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.status

class Address(models.Model):
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)  # or province
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state}, {self.postal_code}, {self.country}"

class Listing(models.Model):
    title = models.CharField(max_length=200)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    map_iframe = models.CharField(max_length=500, blank=True)
    monthly_rent = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sqft = models.IntegerField()
    description = models.TextField(blank=True)
    rules_and_terms = models.ManyToManyField(Rules_Terms, blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    contact = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    move_in_cost = models.ManyToManyField(Move_In_Cost, blank=True)
    property_status = models.ForeignKey(Property_Status, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title