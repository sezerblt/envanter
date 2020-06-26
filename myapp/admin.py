from django.contrib import admin
from .models import Building,Apartment,Furniture,Room
# Register your models here.
admin.site.register(Building)
admin.site.register(Apartment)
admin.site.register(Furniture)
admin.site.register(Room)
