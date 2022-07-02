from django.contrib import admin
from django.urls import path, include
from first_app.views import inicio, AddressViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"address", AddressViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio),
    path("", include("first_app.urls")),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
