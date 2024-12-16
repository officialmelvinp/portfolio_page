
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Portfolio by Melvin-P"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("design.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


