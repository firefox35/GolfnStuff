from django.urls import path, include
from . import views


urlpatterns = [
    path('lesson/', views.lesson, name='lessons'),
    
]