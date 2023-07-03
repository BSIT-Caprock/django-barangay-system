from django.db import models
from django.utils.translation import gettext_lazy as _

# QuerySets

class HouseholdQuerySet(models.QuerySet):

    def household_count(self):
        return self.count()

class IndividualQuerySet(models.QuerySet):
    
    def resident_count(self):
        return self.count()


# Create your models here.

class Household(models.Model):
    household_number = models.CharField(_("Household Number"), max_length=50)
    date_accomplished = models.DateField(_("Date Accomplished"), auto_now=False, auto_now_add=False)
    prepared_by = models.CharField(_("Prepared by (Name of Household Head/Member"), max_length=50)
    certified_by = models.CharField(_("Certified Correct (Barangay Secretary)"), max_length=50)
    validated_by = models.CharField(_("Validated by (Punong Barangay)"), max_length=50)

    objects = HouseholdQuerySet.as_manager()

    def __str__(self):
        return self.household_number


class Individual(models.Model):
    last_name = models.CharField(_("Last Name"), max_length=50, null=True, blank=True)
    first_name = models.CharField(_("First Name"), max_length=50, null=True, blank=True)
    middle_name = models.CharField(_("Middle Name"), max_length=50, null=True, blank=True)
    extension_name = models.CharField(_("Extension Name"), max_length=50, null=True, blank=True)
    place_of_birth = models.CharField(_("Place of Birth"), max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False)
    sex = models.CharField(_("Sex"), max_length=50)
    civil_status = models.CharField(_("Civil Status"), max_length=50, null=True, blank=True)
    citizenship = models.CharField(_("Citizenship"), max_length=50, null=True, blank=True)
    occupation = models.CharField(_("Occupation"), max_length=50, null=True, blank=True)
    house_no = models.CharField(_("House No."), max_length=50, null=True, blank=True)
    street_name = models.CharField(_("Street Name"), max_length=50, null=True, blank=True)
    area_name = models.CharField(_("Subdivion Name/Zone/Sitio/Purok"), max_length=50, null=True, blank=True)
    date_accomplished = models.DateField(_("Date Accomplished"), auto_now=False, auto_now_add=False, null=True, blank=True)
    accomplished_by = models.CharField(_("Name of Person Accomplishing the Form"), max_length=50, null=True, blank=True)
    attested_by = models.CharField(_("Attested by (Barangay Secretary)"), max_length=50, null=True, blank=True)
    household_number = models.CharField(_("Household Number"), max_length=50, null=True, blank=True)
    household = models.ForeignKey(Household, verbose_name=_("Household"), on_delete=models.CASCADE, related_name="members", null=True, blank=True)

    objects = IndividualQuerySet.as_manager()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"