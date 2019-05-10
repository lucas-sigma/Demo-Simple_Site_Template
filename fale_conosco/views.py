from django.shortcuts import render

from . import views

def fale_conosco(request):
    return render(request, 'fale_conosco.html')