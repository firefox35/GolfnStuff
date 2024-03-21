from django.urls import path, include
from .views import (Contact, AddContact)
from . import views


urlpatterns = [
    path('', Contact.as_view(), name='contact'),
    path('add_contact/', AddContact.as_view(), name='add_contact'),  
]