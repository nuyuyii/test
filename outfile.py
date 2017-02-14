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
    "dtr":[],"txx":[],"tnx":[],"txn":[],"tnn":[],"tn10p":[],"tx10p":[],"tn90p":[],
    "tx90p":[],"rx1day":[],"rx5day":[],"sdii":[],"r10mm":[],"r20mm":[],"rnnmm":[],
    "cdd":[],"cwd":[],"r95ptot":[],"r99ptot":[],"prcptot":[]}} 

coordinate = {
    "coor":[]
}

ind_su =[]
pic = []

for x in range(0,1):#len(lons[0:253])):
    for y in range(0,1):#len(lats[0:191])):
        clim = climatecal(2007,2009,lats[x],lons[y],str_date)
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
        print(res_rx5day)

        #ind_su.append([str(year),res_su[0]])
        #pic.append([lons[x],lats[y]])

'''for i in range(0,len(ind_su)):
feature['climdex']['2007']['su'] = ind_su[i]'''


#coordinate['coor'] = pic

#print(pic)

out_file = open("index2.json","w")
json.dump(climdex,out_file)

print('---%s seconds---'%(time.time()-start_time))

#print(cut_res)  







