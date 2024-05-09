from django.shortcuts import render
from django.views.generic import (
    TemplateView, CreateView)
from .models import Contact
from django.db.models import Q
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.


class Contact(TemplateView):
    """View home screen"""
    template_name = "contact/contact.html"


class AddContact(CreateView):
    """Add Contact"""
    template_name = "contact/add_contact.html"
    model = Contact
    context_object_name = "contacts"
    form_class = ContactForm
    success_url = "/contact/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddContact, self).form_valid(form)
