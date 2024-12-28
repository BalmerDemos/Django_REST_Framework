"""
URL configuration for learning_drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Import the Django admin site functionality.
from django.urls import path, include  # Import functions to define URL patterns and include other URL configurations.

# Define the URL patterns for the project.
urlpatterns = [
    path('admin/', admin.site.urls),
    # Maps the `/admin/` URL to the Django admin interface. This is where superusers can manage the app's data.

    path('api/', include('crud_app.urls')),
    # Maps the `/api/` URL prefix to the URL patterns defined in the `crud` app's `urls.py`.
    # This allows all endpoints from the `crud` app to be accessible under `/api/`.
]
