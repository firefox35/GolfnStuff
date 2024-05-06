from django.shortcuts import render
from django.views.generic import (
    TemplateView, CreateView)
from .models import Lessons
from django.template import loader
from django.http import HttpResponse
from .forms import LessonForm
import datetime

# Create your views here.

class Lesson(TemplateView):
    """View home screen"""
    template_name = "lesson/lesson.html"
    

class AddLesson(CreateView):
    """Add Contact"""
    template_name = "lesson/lessons.html"
    model = Lessons
    context_object_name = "lesson"
    form_class = LessonForm
    success_url = "/lessons/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddLesson, self).form_valid(form)

