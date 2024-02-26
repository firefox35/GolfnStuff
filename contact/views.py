from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.

def contact(request):
    if request.method=="POST":
            contact=Contact()
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            comment=request.POST.get('comment')
            contact.name=name
            contact.email=email
            contact.phone=phone
            contact.comment=comment
            contact.save()
            return HttpResponse("<h1>Thanks for contacting us, we will response shortly.</h1>")
    return render(request, 'contact/contact.html')
