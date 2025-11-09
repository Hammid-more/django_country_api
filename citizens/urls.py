from django.urls import path
from .views import CitizenListCreateView, CitizenRetrieveUpdateDestroyView

urlpatterns = [
    path('', CitizenListCreateView.as_view(), name='citizen-list'),
    path('<int:pk>/', CitizenRetrieveUpdateDestroyView.as_view(), name='citizen-detail'),
]
