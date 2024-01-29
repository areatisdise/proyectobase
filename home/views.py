from django.shortcuts import render, redirect
from django.http import HttpResponse
#from .models import TipoCambio,Producto# Import the task function from tasks.py
#from .forms import RUCForm,ProductoForm
#import requests
#import json
from django.http import JsonResponse
from user.models import User


# Create your views here.
def index(request):
    title = 'HOME'
    return render(request, 'index.html', {
        'title': title
    })

def forms(request):
    title = 'FORMS'
    return render(request, 'forms.html', {
        'title': title
    })



