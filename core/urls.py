from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet

from django.urls import path, include

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

# The API URLs are now determined automatically by the router.
# Override the default URL patterns for update and delete actions
urlpatterns = [
    path('customers/update/<str:email>/', CustomerViewSet.as_view({'put': 'update'}), name='customer-update-by-email'),
    path('customers/delete/<str:email>/', CustomerViewSet.as_view({'delete': 'destroy'}), name='customer-delete-by-email'),
    path('', include(router.urls)),
]