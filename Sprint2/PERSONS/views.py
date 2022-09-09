from http.client import HTTPResponse
from django.shortcuts import render

def Login(request):
    return HTTPResponse("Bienvenido a el Projecto de hospitalizacion en casa")