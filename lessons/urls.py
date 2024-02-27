from django.urls import path, include
from . import views


urlpatterns = [
    path('lessons/', views.lesson, name='lessons'),
]