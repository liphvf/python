from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # por baixo ele ainda usa httpresponse
    return render(request, 'home.html', {'usuario': 'fulano de tal'})
