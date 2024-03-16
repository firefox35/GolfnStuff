from django.shortcuts import render
from .models import Lessons
from django.template import loader
from django.http import HttpResponse


# Create your views here.

def lesson(request):
    if request.method=="POST":
            lesson=Lessons()
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            golfer=request.POST.get('golfer')
            date=request.POST.get('date')
            time=request.POST.get('time')
            comment=request.POST.get('comment')
            lesson.name=name
            lesson.email=email
            lesson.golfer=golfer
            lesson.phone=phone
            lesson.date=date
            lesson.time=time
            lesson.comment=comment
            lesson.save()
            return render(request,'lesson/lesson.html')
    return render(request, 'lesson/lessons.html')


