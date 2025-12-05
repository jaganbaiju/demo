from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("This is About Page")

def contact(request):
    return HttpResponse("Contact")

def delete(request):
    return HttpResponse("deleted")

def details(request):
    return HttpResponse("no details")

def detailsssss(request):
    return HttpResponse("no details")

def loc(request):
    return "hrllo"