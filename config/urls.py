
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Portfolio by Melvin-P"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("design.urls")),
]
