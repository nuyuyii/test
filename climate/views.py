from django.shortcuts import render, redirect
from django.core import serializers
from django.template import loader, Context
from django.http import JsonResponse
from netCDF4 import Dataset
from decimal import *

from climate.readNetcdf import ReedNCFile
from climate.r1 import Climdex


import csv
import json
import numpy as np
import datetime as dt

def map(request):
    readNetcdf = ReedNCFile()
    lon = readNetcdf.lon_data(1)
    lat = readNetcdf.lat_data(1)
    return render(request, 'mapVitual.html')#, {'lon':json.dumps(lat)})

def data_ltln(request):
    readNetcdf = ReedNCFile()
    lon = readNetcdf.lon_data(1)
    lat = readNetcdf.lat_data(1)
    asl = json.dumps(lat)
    #print(readNetcdf.lon_data(1))
    #lat = readNetcdf.lat_data(1)
	#return redirect('vitual')#, {'lat':json.dumps(lat)})
    return JsonResponse(lat, safe=False)

def home_page(request):
    cli = Climdex("/home/nuyuyii/401_Project/seaclid/ec85indcal.csv")
    if request.method == 'POST':
        #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        txx_data = cli.txx()
        if request.is_ajax():
            #Always use get on request.POST. Correct way of querying a QueryDict.
            path_file = request.POST.get('path_file')
            print(path_file)
           
            data = {"path_file":getattr(cli, path_file)()}
    
            #Returning same data back to browser.It is not possible with Normal submit
            return JsonResponse(data)
    return render(request, 'home.html')
