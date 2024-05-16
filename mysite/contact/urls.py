# contact/urls.py
from django.urls import path
# Import the thank_you function-based view
from .views import contact, thank_you

urlpatterns = [
    path('contact/', contact, name='contact'),
    # Use thank_you as a function-based view
    path('thank_you/', thank_you, name='thank_you'),
    # Add other URL patterns if needed
]
