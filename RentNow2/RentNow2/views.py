from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def home(request):

    #nombre = "Kevin"
    #apellido = "Tascon"

    #doc_externo = open('C:/Users/usuario/Desktop/RentNow2/RentNow2/Templates/home.html')

    #plt = Template(doc_externo.read())

    #doc_externo.close()

    #doc_externo = loader.get_template('home.html')

    #ctx = Context({"nombre_persona" : nombre , "apellido_persona" : apellido})

    #documento = doc_externo.render({"nombre_persona" : nombre , "apellido_persona" : apellido})

    return render(request, "home.html")#"home.html", {"nombre_persona" : nombre , "apellido_persona" : apellido})


def register(request):

    return render(request, "register.html")


def login(request):

    return render(request, "login.html")