from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Optional simple homepage view
def home(request):
    return JsonResponse({
        "message": "Welcome to Django Country API",
        "endpoints": {
            "citizens": "/citizens/"
        }
    })

urlpatterns = [
    path('', home),  # ✅ handles root URL
    path('admin/', admin.site.urls),
    path('citizens/', include('citizens.urls')),  # ✅ include your app's URLs here
]
