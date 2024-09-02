from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def proyectos (request):
    return render(request, 'proyectos.html')


def base3(request):
    return render(request, 'base3.html')