"""brgy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from brgy.core import views as core_views

urlpatterns = [
    # admin site
    path("admin/", admin.site.urls),
    
    # urls for tabler
    path("", include("admin_tabler.urls")),
    
    # our patterns must be last to override previous routes
    path("", core_views.index, name="index"),
    path("rbi/", core_views.rbi, name="rbi"),
    path("docreq/", core_views.document_requests, name="document_requests"),

    # auto reload browser
    path("__reload__/", include("django_browser_reload.urls")),
]
