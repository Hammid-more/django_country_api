from django.urls import path
from . import views

urlpatterns = [
    path('', views.citizen_list, name='citizen_list'),
    path('<int:id>/', views.citizen_detail, name='citizen_detail'),
]


