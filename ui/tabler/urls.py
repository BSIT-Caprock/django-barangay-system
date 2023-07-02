"""URL Configuration

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

from django.urls import path, include

from .views import household, individual

urlpatterns = [
    # household
    path("households/", household.records, name="household_records"),
    path("households/new/", household.create, name="household_create"),
    path("households/<int:pk>/update/", household.update, name="household_update"),
    path("households/<int:pk>/delete/", household.delete, name="household_records"),

    # individual
    path("individuals/", individual.records, name="individual_records"),
    path("individuals/new/", individual.create, name="individual_create"),
    path("individuals/<int:pk>/update/", individual.create, name="individual_update"),
    path("individuals/<int:pk>/delete/", individual.create, name="individual_delete"),
]
