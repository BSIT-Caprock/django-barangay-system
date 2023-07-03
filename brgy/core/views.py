from django.shortcuts import render

def index(request):
    context = {
        'parent': 'layout',
        'segment': 'index',
    }
    return render(request, "pages/index.html", context)

def dashboard(request):
    context = {
        'parent': 'layout',
        'segment': 'layout_vertical',
    }
    return render(request, "pages/dashboard.html", context)

def rbi(request):
    context = {
        'parent': 'rbi',
        'segment': 'none',
    }
    return render(request, "pages/rbi.html", context)

def document_requests(request):
    context = {
        'parent': 'document_requests',
        'segment': 'none',
    }
    return render(request, "pages/document-requests.html", context)