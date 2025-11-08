from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# 👇 This creates a simple welcome message for the root URL
def home(request):
    return JsonResponse({"message": "Welcome to Django Country API"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # 👈 Root URL now returns a message
    path('api/', include('citizens.urls')),  # 👈 Include your app routes here
]
