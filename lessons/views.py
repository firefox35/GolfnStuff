from django.shortcuts import render
from .models import Lessons
from django.template import loader
from django.http import HttpResponse


# Create your views here.

def lesson(request):
    if request.method=="POST":
            new_lesson=Lessons()
            new_lesson.name=request.POST.get('name')
            new_lesson.email=request.POST.get('email')
            new_lesson.phone=request.POST.get('phone')
            new_lesson.golfer=request.POST.get('golfer')
            new_lesson.date=request.POST.get('date')
            new_lesson.time=request.POST.get('time')
            new_lesson.comment=request.POST.get('comment')
            new_lesson.save()
            return render(request,'lesson/lesson.html')
    return render(request, 'lesson/lessons.html')


