from django.contrib import admin
from django.urls import path, include
from results.views import create_render_admin  # adjust import if your app name is different

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('results.urls')),
    path('create-admin/', create_render_admin),  # visit this once to create superuser
]
