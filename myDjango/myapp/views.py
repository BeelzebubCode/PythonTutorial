from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World! YOYO</h1>")

def about(requset):
    return HttpResponse("<h1>About</h1>")

def form(requset):
    return HttpResponse("<h1>Form</h1>")