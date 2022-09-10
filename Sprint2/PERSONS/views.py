from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError

from django.shortcuts import render

def Login(request):

    return HttpResponse("Bienvenido a el Projecto de hospitalizacion en casa")