# citizens/urls.py

from django.urls import path
from .views import CitizenListCreateView

urlpatterns = [
    path('', CitizenListCreateView.as_view(), name='citizen-list'),
]


