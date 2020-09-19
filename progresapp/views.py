from django.shortcuts import render
from .models import *

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')


def databalai(request):
    databalai = Balai.objects.filter(wilayah=1)

    context = {'databalai': databalai}
    return render(request, 'balai.html', context)


def satker(request):
    datasatker = Satker.objects.filter(wilayah=1)
    context = {'datasatker': datasatker}
    return render(request, 'satker.html', context)


def paket(request):
    datapaket = Paket.objects.filter(wilayah=1)
    context = {'datapaket': datapaket}
    return render(request, 'paket.html', context)