from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ A view to display all products in the cart """

    return render(request,'cart/cart.html')
