from django.shortcuts import render
from django.http import HttpResponse

def _home(request):
    return render(request, "home.html")

def _sobre(request):
    return render(request, "sobre.html")


def _contato(request):
    return render(request, "contato.html")
