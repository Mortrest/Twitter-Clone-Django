from django.urls import path
from .views import *


urlpatterns = [
    path('', homePage, name='home'),
    path('like/<int:pk>', likeFunction, name = 'like'),
    path('like/<int:pk>', likeFunctionFollow, name = 'likeF'),
    path('profile/<int:pk>', profilePage, name = 'profile'),
    path('profile/<int:pk>/follow', followFunction, name = 'follow'),


]
