from django.shortcuts import render  # Import Django's render function (not used here but included by default).

# Importing necessary modules from Django REST Framework and the application.
from rest_framework import viewsets  # Provides a complete set of CRUD operations for a model.
from .models import Item  # Importing the `Item` model to interact with the database.
from .serializers import ItemSerializer  # Importing the serializer to handle data transformation.
from rest_framework.views import APIView  # Base class for defining API views.
from rest_framework.response import Response  # Used to construct API responses.
from rest_framework import status  # Defines HTTP status codes for API responses.

# ViewSet for the Item model, providing all CRUD operations automatically.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# APIView for listing and creating items.
class ItemListCreate(APIView):
    # Handles GET requests to retrieve all items.
    def get(self, request):
        items = Item.objects.all()  # Retrieve all items from the database.
        serializer = ItemSerializer(items, many=True)  # Serialize the queryset into a list of JSON objects.
        return Response(serializer.data)  # Return the serialized data as a response.

    # Handles POST requests to create a new item.
    def post(self, request):
        serializer = ItemSerializer(data=request.data)  # Deserialize the incoming data.
        if serializer.is_valid():  # Validate the data.
            serializer.save()  # Save the new item to the database.
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created item's data.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Return validation errors if the data is invalid.

# APIView for retrieving, updating, and deleting a specific item.
class ItemDetail(APIView):
    # Handles GET requests to retrieve a specific item by its primary key (pk).
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)  # Fetch the item with the specified pk.
        serializer = ItemSerializer(item)  # Serialize the item.
        return Response(serializer.data)  # Return the serialized data as a response.

    # Handles PUT requests to update an existing item by its pk.
    def put(self, request, pk):
        item = Item.objects.get(pk=pk)  # Fetch the item with the specified pk.
        serializer = ItemSerializer(item, data=request.data)  # Deserialize and validate incoming data.
        if serializer.is_valid():  # Check if the data is valid.
            serializer.save()  # Save the updated item to the database.
            return Response(serializer.data)  # Return the updated item's data.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Return validation errors if the data is invalid.

    # Handles DELETE requests to delete a specific item by its pk.
    def delete(self, request, pk):
        item = Item.objects.get(pk=pk)  # Fetch the item with the specified pk.
        item.delete()  # Delete the item from the database.
        return Response(status=status.HTTP_204_NO_CONTENT)
        # Return a 204 No Content status to indicate successful deletion.

