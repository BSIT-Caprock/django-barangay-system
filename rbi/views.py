from django.shortcuts import render

#from django.template.response import TemplateResponse

from django.http import HttpResponse

from . import models


def hello_world(request):
    return HttpResponse('Hello world!')

# Create your views here.

def household_list(request):
    pass

def individual_list(request):
    return render(request, "rbi/individual_list.html")

def individual_create(request):
    if request.method == "POST":
        pass
    pass

    return render(request, "rbi/individual_create.html", {})