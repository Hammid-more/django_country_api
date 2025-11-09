from django.contrib import admin
from django.urls import path, include
from citizens.views import CitizenListCreateView  # ✅ import DRF view

urlpatterns = [
    # ✅ Root URL will show the citizens list directly
    path('', CitizenListCreateView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('citizens/', include('citizens.urls')),
]
