# Generated by Django 3.0.7 on 2020-06-26 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buildingName', models.CharField(max_length=20, verbose_name='Bina Ad')),
                ('buildingImage', models.ImageField(default='building.png', upload_to='building_img')),
            ],
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('furnitureName', models.CharField(max_length=30, verbose_name='Eşya')),
                ('furniturePrice', models.FloatField(blank=True, verbose_name='Fiyat')),
                ('furnitureImage', models.ImageField(default='furniture.png', upload_to='furniture_img')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomName', models.CharField(max_length=20, verbose_name='Oda Ad')),
                ('furnitures', models.ManyToManyField(to='myapp.Furniture', verbose_name='Eşya Listesi')),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartmentName', models.CharField(max_length=40, verbose_name='Daire Ad')),
                ('address', models.TextField(blank=True, max_length=150, verbose_name='Adres')),
                ('apartmentImage', models.ImageField(default='apartment.png', upload_to='apartment_img')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Building', verbose_name='Bina')),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Room', verbose_name='Odalar')),
            ],
        ),
    ]
