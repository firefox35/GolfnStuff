from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Review


class ReviewForm(forms.ModelForm):
    """Form to create a review"""

    class Meta:
        model = Review
        fields = [
            "title",
            "product_name",
            "description",
            "image",
            "image_alt",
        ]

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Review Name",
            "product_name": "Product Name",
            "description": "Description",
            "image": "Product Image",
            "image_alt": "Describe Image",
        }