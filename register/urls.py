from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    
    path('', views.basic,name='register'),
    path('delete_element/<int:id>/',views.delete_element,name='delete_element'),
    path('update_element/<int:id>/',views.update_element,name='update_element'),
    path('sign_up/', views.sign_up,name='sign_up'),
    path('sign_in/', views.sign_in,name='sign_in'),

]