from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("This is About Page")

def contact(request):
    return HttpResponse("Contact")

def details(request):
    return HttpResponse("no details")