from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# ✅ Custom browsable API homepage
@api_view(['GET'])
def api_root(request, format=None):
    """
    Welcome to Django Country API — Citizens REST API
    """
    return Response({
        "message": "Welcome to Django Country API 🇳🇬 — Citizens RESTful Endpoint",
        "description": (
            "This API allows you to view, add, edit, and delete citizens.\n\n"
            "Available endpoints:\n"
            " - /citizens/ → List & Create citizens\n"
            " - /citizens/<id>/ → Retrieve, Update, or Delete a citizen"
        ),
        "citizens_endpoint": reverse('citizen-list', request=request, format=format),
        "admin_panel": request.build_absolute_uri('/admin/'),
    })


urlpatterns = [
    path('', api_root, name='api-root'),  # ✅ Home shows API info
    path('admin/', admin.site.urls),
    path('citizens/', include('citizens.urls')),
]
