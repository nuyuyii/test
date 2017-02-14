from climate.models import feature
import json
import numpy as np

from netCDF4 import Dataset
import datetime as dt 
from decimal import *
#-------------------Database Psql----------------------
import random, string, psycopg2,time
from string import ascii_lowercase
from random import randint

#-------------------import R---------------------------
import math, datetime
import rpy2.robjects as ro
from rpy2.robjects.packages import importr

start_time = time.time()
m = Dataset('/media/nuyuyii/DATA/CSIRO_MK/RCP45/csiromk36-rcp45-dd-pr-tas-t2m.200701.nc', 'r')
lon = m.variables['lon']
lat = m.variables['lat']

coord = []
grid = []

# -------------------------------------------------------
# Creat grid and make grid map point, ts and pr
for i in range(0,len(lat)+1):
    for j in range(0,len(lon)+1):
        if (i==0 and j==0):  # begin lon at lat=0
            grid.append([lon[j]-0.11,lat[i]-0.11])
        elif (i==0 and j<len(lon)):
            grid.append([(lon[j-1]+lon[j])/2,lat[i]-0.11])
        elif (i==0 and j==len(lon)): # limit lat at lon=0
            grid.append([lon[j-1]+0.11,lat[i]-0.11])

        elif (i==191 and j==0):  # limit lon at lat=0
            grid.append([lon[j]-0.11,lat[i-1]+0.11])
        elif (i==191 and j<len(lon)):
            grid.append([(lon[j-1]+lon[j])/2,lat[i-1]+0.11])
        elif (i==191 and j==len(lon)): # limit lat at lon=252
            grid.append([lon[j-1]+0.11,lat[i-1]+0.11])

        elif (j==0):
            grid.append([lon[j]-0.11,(lat[i-1]+lat[i])/2])
        elif (j%253==0):
            grid.append([lon[j-1]+0.11,(lat[i-1]+lat[i])/2])
        else:
            grid.append([(lon[j-1]+lon[j])/2,(lat[i-1]+lat[i])/2]) 

        if (i<len(lat) and j<len(lon)):
            lo = float("%.3f" % lon[j])
            la = float("%.3f" % lat[i])
            coord.append([lo,la])

print(len(coord))

# -------------------------------------------------------
# short cut float grid
for i in range(0,len(grid)):
    grid[i][0] = float("%.3f" %  grid[i][0])
    grid[i][1] = float("%.3f" %  grid[i][1])

'''
features = {
    "type": 'FeatureCollection',
    "": [],
}'''

cnt = 0
for i in range(0,len(coord)):
    coordinates = []
    '''
    if (i%48323==48322):
        print(i,cnt,'------------||')'''
    if (i%253==0):
        print(cnt,'----------**')
        cnt = cnt+1
    #coordinates=[[grid[cnt-1],grid[cnt-1]]]
    coordinates=[[grid[cnt-1],grid[cnt+253],grid[cnt+254],grid[cnt],grid[cnt-1]]]
    #p=feature(point=coord[i],climdex={},coordinates=coordinates)
    feature.objects.create(point=coord[i],climdex={},coordinates=coordinates)

    cnt = cnt+1


print('---%s seconds---'%(time.time()-start_time))

