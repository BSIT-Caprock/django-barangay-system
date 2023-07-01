from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Individual(models.Model):
    last_name = models.CharField(_("Last Name"), max_length=50)
    first_name = models.CharField(_("First Name"), max_length=50)
    middle_name = models.CharField(_("Middle Name"), max_length=50)
    extension_name = models.CharField(_("Extension Name"), max_length=50)
    place_of_birth = models.CharField(_("Place of Birth"), max_length=50)
    date_of_birth = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False)
    sex = models.CharField(_("Sex"), max_length=1)
    civil_status = models.CharField(_("Civil Status"), max_length=50)
    occupation = models.CharField(_("Occupation"), max_length=50)
    house_no = models.CharField(_("House No."), max_length=50)
    street_name = models.CharField(_("Street Name"), max_length=50)
    area_name = models.CharField(_("Subdivion Name/Zone/Sitio/Purok"), max_length=50)
    date_accomplished = models.DateField(_("Date Accomplished"), auto_now=False, auto_now_add=False)
    accomplished_by = models.CharField(_("Name of Person Accomplishing the Form"), max_length=50)
    attested_by = models.CharField(_("Attested by (Barangay Secretary)"), max_length=50)
    household_number = models.CharField(_("Household Number"), max_length=50)

