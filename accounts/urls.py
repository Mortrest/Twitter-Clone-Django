from django.urls import path
from .views import *


urlpatterns = [
    path('', homePage, name='home'),
    path('like/<int:pk>', likeFunction, name = 'like'),
    path('like/<int:pk>', likeFunctionFollow, name = 'likeF'),
    path('profile/<int:pk>', profilePage, name = 'profile'),
    path('profile/<int:pk>/follow', followFunction, name = 'follow'),
    path('register/', registerPage, name = 'register'),
    path('login/',loginPage, name = 'login'),
    path('logout/',logoutUser, name= 'logout'),
    path('search/',searchView, name= 'search'),
    path('detail/<int:pk>',detailView, name= 'detail'),


]
