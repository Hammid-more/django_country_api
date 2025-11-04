# citizens/views.py

from rest_framework import generics
from .models import Citizen
from .serializers import CitizenSerializer

class CitizenListCreateView(generics.ListCreateAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer

class CitizenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
