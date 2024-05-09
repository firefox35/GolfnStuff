from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Lessons


class LessonForm(forms.ModelForm):
    """Form to create a review"""
    # DateTimeField
    date = forms.DateTimeField(
            widget=forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': "datetime-local"
                }
            ),
            initial='2023-07-10'
    )

    class Meta:
        model = Lessons
        fields = [
            "name",
            "email",
            "phone",
            "golfer",
            "date",
            "comment",
        ]

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "name": "Full Name",
            "email": "Email",
            "phone": "Phone No",
            "golfer": "Golf Professional",
            "date": "Appointment Date and Time",
            "comment": "Message",
        }
