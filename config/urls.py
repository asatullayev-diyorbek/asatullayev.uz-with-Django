from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .settings import STATIC_ROOT, STATIC_URL


urlpatterns = [
    path("admin_panel/", admin.site.urls),
    path('', include('public_panel.urls')),
] + static(STATIC_URL, document_root=STATIC_ROOT)
