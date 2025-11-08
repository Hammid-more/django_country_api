from django.urls import path
from . import views

urlpatterns = [
    path('', views.CitizenList.as_view(), name='citizen-list'),  # Example for class-based view
    # OR if you use function-based views:
    # path('', views.citizen_list, name='citizen-list'),
]



