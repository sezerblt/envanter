
from rest_framework import serializers
from .models import Building,Apartment,Furniture,Room
from django.contrib.auth.models import User


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    building = BuildingSerializer(read_only=True)
    building_id = serializers.PrimaryKeyRelatedField(write_only=True, source='building', queryset=Building.objects.all())
    class Meta:
        model = Apartment
        fields ='__all__'


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'


"""
#------------------------------------------------
"""
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Room.objects.all())

    class Meta:
        model = User
        fields = '__all__'
        

class RoomSerializer(serializers.ModelSerializer):
    building = BuildingSerializer(read_only=True)
    building_id = serializers.PrimaryKeyRelatedField(write_only=True, source='building', queryset=Building.objects.all())

    apartment = ApartmentSerializer(read_only=True)
    apartment_id = serializers.PrimaryKeyRelatedField(write_only=True, source='apartment', queryset=Apartment.objects.all())

    furnitures = serializers.PrimaryKeyRelatedField(many=True,queryset=Apartment.objects.all())

    class Meta:
        model = Room
        fields = '__all__'
