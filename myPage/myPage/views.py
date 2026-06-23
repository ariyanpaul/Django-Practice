from django.http import HttpResponse
from django.shortcuts import render



def HomePage(request):
    return render (request, "index.html")

def aboutUs(request):
    return render (request, "aboutus.html")

def contact(request):
    return render (request, "contact.html")