from django.urls import path, include
from .views import (Lesson, AddLesson)
from . import views


urlpatterns = [
    path('', Lesson.as_view(), name='lesson'),
    path('lessons/', AddLesson.as_view(), name='lessons'),
]
