from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Building(models.Model):
    buildingName = models.CharField(max_length=20,verbose_name="Bina Ad")
    buildingImage = models.ImageField(default='building.png', upload_to='building_img')

    def __str__(self):
        return str(self.buildingName)


class Furniture(models.Model):
    furnitureName= models.CharField(max_length=30,verbose_name="Eşya")
    furniturePrice = models.FloatField(verbose_name="Fiyat",blank=True)
    furnitureImage = models.ImageField(default='furniture.png', upload_to='furniture_img')

    def __str__(self):
        return self.furnitureName

class Room(models.Model):
    roomName=models.CharField(max_length=20,verbose_name="Oda Ad")
    furnitures = models.ManyToManyField(Furniture,verbose_name="Eşya Listesi")

    def __str__(self):
        return self.roomName

class Apartment(models.Model):
    apartmentName = models.CharField(max_length=40, verbose_name="Daire Ad")
    address = models.TextField(max_length=150, verbose_name="Adres", blank=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name="Bina")
    rooms = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Odalar")
    apartmentImage = models.ImageField(default='apartment.png', upload_to='apartment_img')

    def __str__(self):
            return str(self.apartmentName)

    def get_absolute_url(self):
        return reverse('apartment_detail', kwargs={'pk': self.pk})


