from django.shortcuts import render
from django.http import HttpResponse

def login(req):
    return render(req, 'login.html')

def inicio(req):
    return render(req, 'index.html')

def descripcion(req):
    return render(req, 'descripcion.html')

def cursos(req):
    return render(req, 'cursos.html')

def contactanos(req):
    return render(req, 'contactanos.html')
