from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return render(request, 'hello/index.html')

def detalhes(request):
    return render(request, 'hello/detalhes.html')
