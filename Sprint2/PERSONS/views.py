import json
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError

from django.shortcuts import render

from .models import patients

def Login(request):

    return HttpResponse("Bienvenido a el Projecto de hospitalizacion en casa")

def Newpatient(request):
    if request.method == 'POST':
        try:
            data= json.loads(request.body)
            patient = patients(
                patientid = data["patientid"],
                patientfirstname = data["patientfirstname"],
                patientlastname= data["patientlastname"],
                patientphonenumber = data["patientphonenumber"],
                patientgender = data["patientgender"],
                patientaddress = data["patientaddress"],
                patientcity = data["patientcity"],
                patientBirthday = data["patientBirthday"],
                patientLatitude = data["patientLatitude"],
                patientLongitude = data["patientLongitude"]
            )
            patient.save()
            return HttpResponse("paciente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método invalido")