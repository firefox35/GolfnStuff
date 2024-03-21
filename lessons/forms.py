from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Lessons


class LessonForm(forms.ModelForm):
    """Form to create a review"""
    
    class Meta:
        model = Lessons
        fields = [
            "name",
            "email",
            "phone",
            "golfer",
            "date",
            "time",
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
            "date": "Appointment Date",
            "time": "Appointment Time",
            "comment": "Message",
            
        }