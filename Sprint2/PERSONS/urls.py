
from pydoc import visiblename
from sys import path_hooks
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home',views.Login,name=''),
    path('newdoctor', views.newdoctor, name ='Nuevo doctor'),
    path('newpatient', views.newpatient, name='Nuevo paciente'),
    path('newhelper', views.newhelper, name='Nuevo ayudante'),
    path('viewpatients', views.getpatients, name='Obtener pacientes'),
    path('viewpatients/<int:id>', views.getexclusivepatient, name="Obtener un paciente")
]