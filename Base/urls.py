from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.userLogout, name="logout"),
    path('home/', views.home, name="home"),
    path('room/<str:pk>', views.room, name="room"),
    path('roomForm', views.createRoom, name="room_form"),
    path('roomForm/<str:pk>', views.updateRoom, name="room_form"),
    path('deleteRoom/<str:pk>', views.deleteRoom, name="delete_room"),
]
