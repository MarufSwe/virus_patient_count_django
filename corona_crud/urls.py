from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.add_patient, name='add-patient'),  # get and post request for insert operation

    path('edit-patient/<int:id>/', views.update_patient, name='patient_update'),  # get and post request for update operation

    path('delete/<int:id>', views.patient_delete, name='patient_delete'),  # get and post request for update operation

    path('list/', views.patient_list, name='patient_list'),  # get request to retrive and display all data

    path('date', views.date_picker),  # get request to retrive and display all data
    # path('district/', views.district)
]
