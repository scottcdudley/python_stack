from django.shortcuts import render, HttpResponse, redirect

def index(request):
  response = "placeholder to later diplay all the list of blogs" 
  return HttpResponse(response)
def new (request):
  response = "placeholder to display a new form to create a new blog"
  return HttpResponse(response)
def create(request):
  return redirect ('/')
def show(request, number):
  print (number)
  return HttpResponse("show method" + number )
def edit(request, number):
  print (number)
  return HttpResponse("show method" + number )
def destroy(request, number):
  return redirect('/')