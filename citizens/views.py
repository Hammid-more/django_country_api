from rest_framework import generics
from .models import Citizen
from .serializers import CitizenSerializer


# ✅ List all citizens or create a new one
class CitizenListCreateView(generics.ListCreateAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer


# ✅ Retrieve, update, or delete a citizen
class CitizenRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
