from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet

from django.urls import path, include

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]