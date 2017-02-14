from climate.models import feature
# p=LatLon({"type": 'FeatureCollection',"features":[ 100000.9],})

#LatLon.objects.create(longitude=11.0001, latitude=11.0001,climdex={"rx5day":  [1,2,3]})
#climdex['rx5day'][0]
#p=LatLon(point={'point':[1,2]},climdex={"rx5day":  [1,2,3]})
#o=feature.objects.get(pk=6)
#print(o.climdex)
import json
import os
import numpy as np

from netCDF4 import Dataset
# import matplotlib.pyplot as plt
import time 
import math, datetime
from decimal import *

from database import climatecal #-------------



lat1 = 122
lon1 = 222
str_date = "2006-12-31"


#result = clim.prcptot()

m = Dataset('/media/nuyuyii/DATA/CSIRO_MK/RCP45/csiromk36-rcp45-dd-pr-tas-t2m.200701.nc', 'r')
lons = m.variables['lon']
lats = m.variables['lat']

c = np.array(lons[:])
lons = [float(Decimal("%.2f" % e)) for e in c]

c = np.array(lats[:])
lats = [float(Decimal("%.2f" % e)) for e in c]

#print(m.variables)
cut_res = []
#print(len(lons[:]))
count = 1

res_date = []

start_time = time.time()

year = 2007

climdex = {"2007":{"su":[],"fd":[],"id":[],"tr":[],"gsl":[],"wsdi":[],"csdi":[],
    "dtr":[],"txx":[],"tnx":[],"txn":[],"tnn":[],"tn10p":[],"tx10p":[],"tx10p":[],
    "tx90p":[],"rx1day":[],"rx5day":[],"sdii":[],"r10mm":[],"r20mm":[],"rnnmm":[],
    "cdd":[],"cwd":[],"r95ptot":[],"r99ptot":[],"prcptot":[]}} 

coordinate = {
    "coor":[]
}

ind_su =[]
pic = []

eindex={"su","fd","id","tr","gsl","wsdi","csdi","dtr","txx","tnx","txn","tnn","tn10p","tx10p","tx10p","tx90p","rx1day","rx5day","sdii","r10mm","r20mm","rnnmm","cdd","cwd","r95ptot","r99ptot","prcptot"}
eyear={"2007","2008","2009"}

print(eindex[1])
'''
for x in range(0,1):#len(lons[0:253])):
    for y in range(0,1):#len(lats[0:191])):
        clim = climatecal(2007,2009,lats[y],lons[x],str_date)
        res_cwd = clim.cwd()

        res_su = clim.su()
        res_fd = clim.fd()
        res_id = clim.id()
        res_tr = clim.tr()
        res_gsl = clim.gsl()
        res_wsdi = clim.wsdi()
        res_csdi = clim.csdi()
        res_dtr = clim.dtr()
        res_txx = clim.txx()
        res_tnx = clim.tnx()
        res_txn = clim.txn()
        res_tnn = clim.tnn()
        res_tn10p = clim.tn10p()
        res_tx10p = clim.tx10p()
        res_tn90p = clim.tn90p()
        res_tx90p = clim.tx90p()
        res_rx1day = clim.rx1day()
        res_rx5day = clim.rx5day()
        res_sdii = clim.sdii()
        res_r10mm = clim.r10mm()
        res_r20mm = clim.r20mm()
        res_rnnmm = clim.rnnmm()
        res_cdd = clim.cdd()
        res_r95ptot = clim.r95ptot()
        res_r99ptot = clim.r99ptot()
        res_prctot = clim.prcptot()
        
        climdex['2007']['su'] = res_su[0]
        climdex['2007']['fd'] = res_fd[0]
        climdex['2007']['id'] = res_id[0]
        climdex['2007']['tr'] = res_tr[0]
        climdex['2007']['gsl'] = res_gsl[0]
        climdex['2007']['wsdi'] = res_wsdi[0]
        climdex['2007']['csdi'] = res_csdi[0]
        climdex['2007']['dtr'] = res_dtr[0]
        climdex['2007']['txx'] = res_txx[0]
        climdex['2007']['tnx'] = res_tnx[0]
        climdex['2007']['txn'] = res_txn[0]
        climdex['2007']['tnn'] = res_tnn[0]
        climdex['2007']['tn10p'] = res_tn10p[0]
        climdex['2007']['tx10p'] = res_tx10p[0]
        climdex['2007']['tn90p'] = res_tn90p[0]
        climdex['2007']['tx90p'] = res_tx90p[0]
        climdex['2007']['rx1day'] = res_rx1day[0]
        climdex['2007']['rx5day'] = res_rx5day[0]
        climdex['2007']['sdii'] = res_sdii[0]
        climdex['2007']['r10mm'] = res_r10mm[0]
        climdex['2007']['r20mm'] = res_r20mm[0]
        climdex['2007']['rnnmm'] = res_rnnmm[0]
        climdex['2007']['cdd'] = res_cdd[0]
        climdex['2007']['cwd'] = res_cwd[0]
        climdex['2007']['r95ptot'] = res_r95ptot[0]
        climdex['2007']['r99ptot'] = res_r99ptot[0]
        climdex['2007']['prcptot'] = res_prctot[0]

        LatLon.objects.create(climdex=feature)
        #ind_su.append([str(year),res_su[0]])
        #pic.append([lons[x],lats[y]])
'''
# IF EXISTS
# drop database dbclimate;
# create database dbclimate with owner projectuser;
# create database dbproject with owner projectuser;
# DROP SCHEMA public CASCADE;
feature.objects.create(point=[1.0005,50.333],climdex={'ts':200},coordinates=[[[2.22,555.22]]])

{'ps':[111.00,2333.0]}
o.climdex
o.coordinates
o.point
climate_feature

Query
select id,point,climdex,coordinates FROM climate_feature WHERE id<5;
print('---%s seconds---'%(time.time()-start_time))
