from django.urls import path, include
from . import views

# Namespace for the accounts app
app_name = 'accounts'

# URL patterns for authentication and registration
urlpatterns = [
    path('', include('django.contrib.auth.urls')),  # Login, logout, password management
    path('register/', views.register, name='register'),  # User registration page
]