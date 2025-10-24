from django.contrib import admin
from django.urls import path, include
from results.views import create_superuser   # <-- Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('results.urls')),
    path('create-admin/', create_superuser),
]
