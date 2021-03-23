from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

# Create your views here.

def register(request):

    return render(request, "register/colorlib-regform-8/register.html")


def login(request):

    return render(request, "login.html")