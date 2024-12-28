from rest_framework import serializers  # Importing DRF's serializers module to handle data transformation and validation.
from .models import Item  # Importing the `Item` model, which will be serialized.

# Defining the serializer for the `Item` model.
class ItemSerializer(serializers.ModelSerializer):
    # A serializer that converts `Item` model instances into JSON format and validates JSON input for creating or updating items.

    class Meta:
        # Metadata for the serializer.
        model = Item
        # Specifies the model to be serialized, in this case, the `Item` model.

        # fields = '__all__'  # Uncomment this line to include all fields from the `Item` model in the serializer.
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
        # Specifies the fields to include in the serialization process. Only these fields will be exposed in the API.
