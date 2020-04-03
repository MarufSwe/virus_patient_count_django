from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import PatientsForm
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# Pagination
def patient_list(request):
    patient_list = Patients.objects.all()
    paginator = Paginator(patient_list, 2)  # Show 2 contacts per page.
    page_number = request.GET.get('page')
    patient_list = paginator.get_page(page_number)
    context = {'patient_list': patient_list}
    return render(request, 'patients_register/patients_list.html', context)


# Add Patient
def add_patient(request):
    if request.method == 'POST':
        patient_add_form = PatientsForm(request.POST, request.FILES)

        if patient_add_form.is_valid():
            patient_add_form.save()
            return redirect('patient_list')
    else:
        patient_add_form = PatientsForm()

    template = 'patients_register/patient_form.html'
    context = {'form': patient_add_form}
    return render(request, template, context)


# Edit Patient
def update_patient(request, id=None):
    query = Patients.objects.get(id=id)
    form = PatientsForm(request.POST or None, instance=query)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('patient_list')
            # return redirect('prescription:prescription-details', id=request.user.id)

    context = {'form': form}
    template = 'patients_register/patient_form.html'

    return render(request, template, context)


# Delete Patient
def patient_delete(request, id):
    patient = Patients.objects.get(pk=id)
    patient.delete()
    return redirect('patient_list')


def date_picker(request):
    return render(request, 'patients_register/DatePicker.html')

# pagination
# class Paitents():
#     model = User
#     template_name = 'core/user_list.html'  # Default: <app_label>/<model_name>_list.html
#     context_object_name = 'users'  # Default: object_list
#     paginate_by = 10
#     queryset = User.objects.all()  # Default: Model.objects.all()
