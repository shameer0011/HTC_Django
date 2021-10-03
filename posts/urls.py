from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('addposts/', views.addpost,name="posts-AddPost"),

]