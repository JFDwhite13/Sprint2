import json
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError

from django.shortcuts import render

from .models import doctorandnurse, helper, patients

def Login(request):

    return HttpResponse("Bienvenido a el Projecto de hospitalizacion en casa\n Para agregar a un paciente ve a /newpatient\n Para agregar a un nuevo doctor ve a /newdoctor\n Para agregar un nuevo ayudante o encargado ve a /newhelper\n\n Para consultar")

def newpatient(request):
    if request.method == "POST":
        print("method:", request.method)
        try:
            data = json.loads(request.body)
            print(data)
            patient = patients(
                patientid = data["patientid"],
                patientfirstname = data["patientfirstname"],
                patientlastname = data["patientlastname"],
                patientphonenumber = data["patientphonenumber"],
                patientgender = data["patientgender"],
                patientaddress = data["patientaddress"],
                patientcity = data["patientcity"],
                patientBirthday = data["patientBirthday"],
                patientLatitude = data["patientLatitude"],
                patientLongitude = data["patientLongitude"]
            )
            print(patient)
            patient.save()
            return HttpResponse("paciente agregado")
        except:
            return HttpResponseBadRequest("Datos invalidos")
    elif request.method == "GET":
        return HttpResponseNotAllowed(['POST'], "Para agregar un paciente debes usar POST")
    else:
        return HttpResponseNotAllowed(['POST'], "METODO NO PERMITIDO")


def newdoctor(request):
    if request.method == "POST":
        print("method:", request.method)
        try:
            data = json.loads(request.body)
            print(data)
            doctor = doctorandnurse(
                dnid = data["dnid"] ,
                dFirstname = data["dFirstname"] ,
                dLastname= data["dLastname"] ,
                dPhoneNumber = data["Telefono"] ,
                dgender=data["dgender"] ,
                dspecialty=data["dspecialty"] ,
                dresgister=data["dresgister"] ,
                isdoctor= data["isdoctor"]
            )
            doctor.save()
            return HttpResponse("Doctor agregado")
        except:
            return HttpResponseBadRequest("Datos invalidos")
    elif request.method == "GET":
        return HttpResponseNotAllowed(['POST'], "Para agregar un Doctor debes usar POST")
    else:
        return HttpResponseNotAllowed(['POST'], "METODO NO PERMITIDO")

def newhelper(request):
    if request.method == "POST":
        print("method:", request.method)
        try:
            data = json.loads(request.body)
            print(data)
            helperson = helper(
                hid = data["hid"],
                hfirstname = data["hfirstname"],
                hlastname = data["hlastname"],
                hphoneNumber = data["hphoneNumber"],
                hgender = data["hgender"],
                hidpatient =  patients.objects.get(patientid = data["hidpatient"]),
                hkinship = data["hkinship"],
                hemail = data["hemail"]
            )
            print(helperson)
            helperson.save()
            return HttpResponse("Ayudante agregado")
        except:
            return HttpResponseBadRequest("Datos invalidos revise la cedula del paciente o demas datos")
    elif request.method == "GET":
        return HttpResponseNotAllowed(['POST'], "Para agregar un Ayudante debes usar POST")
    else:
        return HttpResponseNotAllowed(['POST'], "METODO NO PERMITIDO")

def getpatients(request):
    if request.method == 'GET':
        try:
            patientlist = patients.objects.all()
            if (not patients):
                return HttpResponseBadRequest("No existen usuarios cargados")
            allpatientsdata=[]
            for pat in patientlist:
                data ={"patientid":pat.patientid,"patientfirstname":pat.patientfirstname, "patientlastname":pat.patientlastname, "patientphonenumber" :pat.patientphonenumber,"patientgender":pat.patientgender, "patientaddress":pat.patientaddress,"patientcity":pat.patientcity,"patientBirthday":pat.patientBirthday,"patientLatitude":pat.patientLatitude,"patientLongitude":pat.patientLongitude}
                allpatientsdata.append(data)
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(allpatientsdata)
            return resp
        except:
            return HttpResponseBadRequest
    else:
        return HttpResponseNotAllowed(['GET'], "Metodo no permitido")

def getexclusivepatient(request, id):
    if request.method == 'GET':
       # try:
            
            patient = patients.objects.filter(patientid = id)
            print(patient)
            if (not patient):
                return HttpResponseBadRequest("No existe un paciente con ese documento.")
            
            allpatientdata=[]
            for pat in patient:
                data ={"patientid":pat.patientid,"patientfirstname":pat.patientfirstname, "patientlastname":pat.patientlastname, "patientphonenumber" :pat.patientphonenumber,"patientgender":pat.patientgender, "patientaddress":pat.patientaddress,"patientcity":pat.patientcity,"patientBirthday":pat.patientBirthday,"patientLatitude":pat.patientLatitude,"patientLongitude":pat.patientLongitude}
                allpatientdata.append(data)
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(allpatientdata)
            return resp
        #except:
            #return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

