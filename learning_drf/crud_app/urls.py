from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, ItemListCreate, ItemDetail

# Create a router instance to automatically generate URL patterns for the viewsets.
router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')  # Registering the 'ItemViewSet' with the route prefix 'items'.

# Define URL patterns for the app.
urlpatterns = [
    path('', include(router.urls)),  # Include all automatically generated URLs from the router.
    path('items/', ItemListCreate.as_view(), name='item-list-create'),  # URL for listing all items or creating a new one.
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),  # URL for retrieving, updating, or deleting a specific item by ID.
]
