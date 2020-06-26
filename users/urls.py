from django.contrib import admin
from django.urls import path,include
from .views import register
#from users import views as users_views
from .views import register,profile
urlpatterns = [
    path('',register,name='register_url_name'),
    path('profile',profile,name='profile_url_name'),
]