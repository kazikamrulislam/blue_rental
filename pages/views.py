from django.shortcuts import render
from django.http import HttpResponse

def  index(request):
    return render(request, 'pages/index.html')

def  applications(request):
    return render(request, 'pages/applications.html')