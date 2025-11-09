from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


# ✅ Optional: API root view (nice homepage)
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'citizens': reverse('citizen-list', request=request, format=format),
    })


urlpatterns = [
    path('', api_root, name='api-root'),  # ✅ browsable API root
    path('admin/', admin.site.urls),
    path('citizens/', include('citizens.urls')),
]
