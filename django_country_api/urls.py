from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Django Country API"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/', include('citizens.urls')),  # 👈 this is the critical line
]
