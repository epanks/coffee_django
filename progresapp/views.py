from django.db import models
from django.shortcuts import render
from django.db.models import F,Sum,ExpressionWrapper,FloatField
from .models import Balai,Satker,Paket
from django.db.models.functions import Cast

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')


def databalai(request):
    # databalai = Balai.objects.filter(wilayah=1)
    databalai = Balai.objects.all()

    context = {'databalai': databalai}
    return render(request, 'balai.html', context)


def satker(request):
    datasatker = Satker.objects.filter(wilayah=1)
    context = {'datasatker': datasatker}
    return render(request, 'satker.html', context)


def paket(request):
    
    datapaket = Paket.objects.filter(wilayah=1).annotate(pagu=Sum(F('rpm')+F('phln')+F('sbsn'),output_field=models.FloatField()))
    context = {'datapaket': datapaket}
    return render(request, 'paket.html', context)
