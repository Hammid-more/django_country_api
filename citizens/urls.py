from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    return redirect('/citizens/')

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('citizens/', include('citizens.urls')),
]
