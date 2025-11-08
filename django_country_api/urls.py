from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# 👇 This creates a simple home route
def home(request):
    return JsonResponse({"message": "Welcome to Django Country API"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # 👈 Root route
    path('api/', include('citizens.urls')),  # 👈 This connects to your citizens app
]
