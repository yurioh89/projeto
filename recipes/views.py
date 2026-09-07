from django.shortcuts import render
from django.http import HttpResponse

def _home(request):
    return render(request, "recipes/pages/home.html")

def _sobre(request):
    return render(request, "recipes/pages/sobre.html")


def _contato(request):
    return render(request, "recipes/pages/contato.html")
