from django.contrib import admin

from .models import *


# Register your models here.

class PatientsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'age', 'father_name', 'mobile', 'email', 'virusName',
                    'suspect_date', 'division_name', 'district', 'patient_img']


# class VirusNameAdmin(admin.ModelAdmin):
#     list_display = ['virus_name']
#
#
# class DivisionAdmin(admin.ModelAdmin):
#     list_display = ['division_name']
#
#
# class DistrictAdmin(admin.ModelAdmin):
#     list_display = ['district_name']


admin.site.register(Patients, PatientsAdmin)
# admin.site.register(VirusName, VirusNameAdmin)
# admin.site.register(Division, DivisionAdmin)
# admin.site.register(District, DistrictAdmin)
admin.site.register(VirusName)
admin.site.register(District)
admin.site.register(Division)
