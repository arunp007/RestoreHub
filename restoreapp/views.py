from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'restore_home.html')

def products(request):
    return render(request, 'products.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def product1(request):
    return render(request, 'product1.html')

def product2(request):
    return render(request, 'product2.html')

def product3(request):
    return render(request, 'product3.html')

def product4(request):
    return render(request, 'product4.html')

def product5(request):
    return render(request, 'product5.html')

def order_now(request):
    return render(request, 'order_now.html')

def order_success(request):
    return render(request, 'order_success.html')

def sell(request):
    return render(request, 'sell.html')