from django.contrib import admin

from rbi import models as rbi

# ModelAdmins

class HouseholdAdmin(admin.ModelAdmin):
    list_display = ("household_number", "date_accomplished", "prepared_by", )


class IndividualAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "middle_name", "household_number")

# Register your models here.

admin.site.register(rbi.Household, HouseholdAdmin)
admin.site.register(rbi.Individual, IndividualAdmin)