from django.shortcuts import render, redirect
app_name="appusers"
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    crypto = Cryptocurrencies_Rate.objects.all()
    giftcard = Giftcard_Rate.objects.all()
    data = {'crypto':crypto,'giftcard':giftcard}
    return render(request, 'index.html', data)
