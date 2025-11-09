from django.urls import path
from . import views

urlpatterns = [
    path('', views.citizen_list, name='citizen-list'),
    path('<int:id>/', views.citizen_detail, name='citizen-detail'),
]
