from django.contrib import admin
from django.urls import include, path
from . import views
from .views import ApartmentListView,ApartmentDetailView,ApartmentCreateView,ApartmentUpdateView,ApartmentDeleteView,home,about
from .views import RoomCreateView,RoomDeleteView
from .views import BuildingCreateView,BuildingDeleteView
from .views import FurnitureCreateView,FurnitureDeleteView
#name prameter's redirect keyword for example
urlpatterns = [
    path('about', views.about, name='about_url_name'),
    path('',                      ApartmentListView.as_view(),name='home_url_name'),  #Redirect('home_url_name')
    path('apartment/<int:pk>/',        ApartmentDetailView.as_view(), name='apartment_detail'),
    path('apartment/new/',             ApartmentCreateView.as_view(), name='apartment_create'),
    path('building/new/',              BuildingCreateView.as_view(),  name='building_create'),
    path('room/new/',                  RoomCreateView.as_view(),      name='room_create'),
    path('furniture/new/',             FurnitureCreateView.as_view(), name='furniture_create'),
    path('apartment/<int:pk>/update/', ApartmentUpdateView.as_view(), name='apartment_update'),
    path('apartment/<int:pk>/delete/', ApartmentDeleteView.as_view(), name='apartment_delete'),
    path('building/<int:pk>/delete/',   BuildingDeleteView.as_view(),  name='building_delete'),
    path('room/<int:pk>/delete/',       RoomDeleteView.as_view(),      name='room_delete'),
    path('furniture/<int:pk>/delete/',  FurnitureDeleteView.as_view(), name='furniture_delete'),

]