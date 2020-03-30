from django import forms
from django.forms import SelectDateWidget

from .models import Patients


class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'
        widgets = {
            'suspect_date': SelectDateWidget(attrs={'class': 'form-control'})
        }
        labels = {'full_name': 'Full Name',
                  'mobile': 'Mobile No',
                  'patient_img': 'Patient Image',
                  'suspect_date': 'Suspect Date'}

    def __init__(self, *args, **kwargs):
        super(PatientsForm, self).__init__(*args, **kwargs)
        self.fields['virusName'].empty_label = "Select"
        self.fields['district'].empty_label = "Select"
        self.fields['suspect_date'].required = False
