from django.urls import path
from recipes.views import _home, _sobre, _contato

urlpatterns = [
    path('', _home),
    path('sobre/', _sobre),
    path('contato/', _contato), 
]