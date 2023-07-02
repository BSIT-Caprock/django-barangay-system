from django.shortcuts import render

from django.template.response import TemplateResponse

from django.http import HttpResponse

# parent directory

BDIR = "tabler"

# use these wrapper functions

def rend(request, template_name, context=None, content_type=None, status=None, using=None):
    return render(request, f"{BDIR}/templates/{template_name}", context, content_type, status, using)

