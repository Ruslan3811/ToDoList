from django.contrib import admin
from django.urls import path, include
from .views import todoappView, addToDoView, delToDoView

urlpatterns = [
    path('todoapp/', todoappView, name='list'),
    path('addToDoItems/', addToDoView, name='add'),
    path('delToDoItems/<int:i>/', delToDoView, name='del'),
]
