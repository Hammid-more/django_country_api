from django.urls import path
from . import views

urlpatterns = [
    path('citizens/', views.citizen_list, name='citizen_list'),          # GET all, POST new
    path('citizens/<int:id>/', views.citizen_detail, name='citizen_detail'),  # GET one, PUT/PATCH, DELETE
]
