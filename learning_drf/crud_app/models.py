from django.db import models  # Importing Django's built-in ORM (Object-Relational Mapping) models.

# Create your models here.
class Item(models.Model):  # Defining the `Item` model, which represents a database table.
    name = models.CharField(max_length=100)  # A character field to store the name of the item with a maximum length of 100 characters.
    description = models.TextField()  # A text field to store a longer description of the item.
    created_at = models.DateTimeField(auto_now_add=True)
    # A datetime field that automatically stores the timestamp when an item is created.
    updated_at = models.DateTimeField(auto_now=True)
    # A datetime field that automatically updates the timestamp whenever the item is modified.

    def __str__(self):
        # A string representation method to define how the object will be displayed as a string.
        return self.name
