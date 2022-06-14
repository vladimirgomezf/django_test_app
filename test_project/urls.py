from django.contrib import admin
from django.urls import path, include
from first_app.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('', include('first_app.urls')),
]
