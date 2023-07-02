from django.urls import path, include
from brgy.core import views as core_views

urlpatterns = [
    path("", core_views.index),
]
