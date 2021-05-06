from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def george(request):
  return HttpResponse("Hey George")

def ruby(request):
  return HttpResponse("Ruby is a good dog!")

def greet(request, name):
  return render(request, "hello/greet.html", {
    "name": name.capitalize()
  })