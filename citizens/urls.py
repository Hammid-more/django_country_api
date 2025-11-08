from django.urls import path
from . import views

urlpatterns = [
    path('', views.citizen_list, name='citizen-list'),
    path('citizens/', views.citizen_list, name='citizen-list-alt'),
]

