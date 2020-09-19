from django.urls import path
from .views import databalai, satker, dashboard, paket

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('balai/', databalai, name='databalai'),
    path('satker/', satker, name='satker'),
    path('paket/', paket, name='paket'),
]
