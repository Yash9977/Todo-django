from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    
    path('', views.basic,name='register'),
    path('delete_element/<int:id>/',views.delete_element,name='delete_element'),

]