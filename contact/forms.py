from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Contact


class ContactForm(forms.ModelForm):
    """Form to create a review"""

    class Meta:
        model = Contact
        fields = [
            "name",
            "email",
            "phone",
            "comment",
        ]

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "name": "Full Name",
            "email": "Email",
            "phone": "Phone No",
            "comment": "Message",
            
        }