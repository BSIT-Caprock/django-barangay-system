from django.contrib import admin

from rbi import models as rbi

# Register your models here.

admin.site.register(rbi.Household)
admin.site.register(rbi.Individual)