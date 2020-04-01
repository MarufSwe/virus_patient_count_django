from django.contrib.admin import options
from django.db import models


# Create your models here.
class VirusName(models.Model):
    virus_name = models.CharField(max_length=25)

    def __str__(self):
        return self.virus_name


class Division(models.Model):
    division_name = models.CharField(max_length=20)

    def __str__(self):
        return self.division_name


class District(models.Model):
    district_name = models.CharField(max_length=20)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.district_name


class Patients(models.Model):
    full_name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    father_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    virusName = models.ForeignKey(VirusName, on_delete=models.CASCADE, null=True, blank=True)
    suspect_date = models.DateField(null=True, blank=True)
    patient_img = models.ImageField(upload_to='patient_images', null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.full_name

    def district_name(self):
        return self.district.district_name

    def virus_name(self):
        return self.virusName.virus_name

    def division_name(self):
        return self.district.division.division_name
