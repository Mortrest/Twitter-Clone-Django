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
    path('detail/<int:pk1>/<int:pk2>',deleteComment, name= 'deleteComment'),
    path('profile/<int:pk>/following',followingList, name= 'followinglist'),
    path('post/<int:pk>/delete',deleteTweet, name= 'deleteTweet'),
    path('post/<int:pk>/deleteD',deleteTweetDetail, name= 'deleteTweetDetail'),
    path('tweet/',tweetPage, name= 'tweet'),
    path('tweet/add/',addTweet, name= 'addTweet'),


]
