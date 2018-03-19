from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, id=None, *args, **kwargs):
    response = "placeholder to display blog {}".format(id)
    return HttpResponse(response)

def edit(request, id=None, *args, **kwargs):
    response = "To edit blog {} later".format(id)
    return HttpResponse(response)

def destroy(request, id=None, *args, **kwargs):
    return redirect('/')