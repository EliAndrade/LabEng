from django.urls import path
from .views import registerPatient, registerExam, listPatients, listExams, listLaudos


urlpatterns = [
    path('cadastrar/paciente', registerPatient, name='registerPatient'),
    path('cadastrar/exame', registerExam, name='registerExam'),
    path('listar/pacientes', listPatients, name='listPatients'),
    path('listar/exames', listExams, name='listExams'),
    path('listar/laudos', listLaudos, name='listLaudos')


]