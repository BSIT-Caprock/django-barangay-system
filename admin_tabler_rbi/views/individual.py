from django.shortcuts import render

#from django.template.response import TemplateResponse

from django.http import HttpResponse

from rbi.models import Individual


# Create your views here.

def records(request):
    return render(request, "rbi/individual_list.html")

def create(request):
    if request.method == "POST":
        pass
    pass

    return render(request, "rbi/individual_create.html", {})

def update(request):
    pass

def delete(request):
    pass