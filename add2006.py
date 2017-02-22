import json
import os
import numpy as np

from climate.models import feature

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

importr("climdex.pcic")
importr("PCICt")


import rpy2.robjects as robjects
#r_source = robjects.r['source']
#r_source("/home/thiranan/Project2/dex1.r")

from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage

string = """
library("climdex.pcic")
library(PCICt)

cal_date <- function(numday,str_date){
  cal <- "365_day"
  origin <- str_date
  seconds.per.day <- 86400
  ts.dat.days <- 1:numday
  origin.pcict <- as.PCICt(origin, cal)
  ts.dat.pcict <- origin.pcict + (ts.dat.days * seconds.per.day)
  return(ts.dat.pcict)
}

mdata <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  c_date <- cal_date(numday,str_date)
  ## Load the data in.
  ci_mydata <- climdexInput.raw(tmax,tmin,pr,c_date,c_date,c_date,base.range=c(str_year, end_year))
  return(ci_mydata)
}

su <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  su_mydata <- climdex.su(ci_mydata)
  su_mydata <- round(su_mydata, digits=2)
  return(su_mydata)
}

fd <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  fd_mydata <- climdex.fd(ci_mydata)
  fd_mydata <- round(fd_mydata, digits=2)
  return(fd_mydata)
}
id <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  id_mydata <- climdex.id(ci_mydata)
  id_mydata <- round(id_mydata, digits=2)
  return(id_mydata)
}
tr <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  tr_mydata <- climdex.tr(ci_mydata)
  tr_mydata <- round(tr_mydata, digits=2)
  return(tr_mydata)
}
gsl <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  gsl_mydata <- climdex.gsl(ci_mydata)
  gsl_mydata <- round(gsl_mydata, digits=2)
  return(gsl_mydata)
}
wsdi <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  wsdi_mydata <- climdex.wsdi(ci_mydata)
  wsdi_mydata <- round(wsdi_mydata, digits=2)
  return(wsdi_mydata)
}
csdi <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  csdi_mydata <- climdex.csdi(ci_mydata)
  csdi_mydata <- round(csdi_mydata, digits=2)
  return(csdi_mydata)
}
dtr <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  dtr_mydata <- climdex.dtr(ci_mydata,freq = c("annual"))
  dtr_mydata <- round(dtr_mydata, digits=2)
  return(dtr_mydata)
}
sdii <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  sdii_mydata <- climdex.sdii(ci_mydata)
  sdii_mydata <- round(sdii_mydata, digits=2)
  return(sdii_mydata)
}
r10mm <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  r10mm_mydata <- climdex.r10mm(ci_mydata)
  r10mm_mydata <- round(r10mm_mydata, digits=2)
  return(r10mm_mydata)
}
r20mm <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  r20mm_mydata <- climdex.r20mm(ci_mydata)
  r20mm_mydata <- round(r20mm_mydata, digits=2)
  return(r20mm_mydata)
}
rnnmm <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  rnnmm_mydata <- climdex.rnnmm(ci_mydata)
  rnnmm_mydata <- round(rnnmm_mydata, digits=2)
  return(rnnmm_mydata)
}
cdd <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  cdd_mydata <- climdex.cdd(ci_mydata)
  cdd_mydata[is.na(cdd_mydata)] <- 0
  cdd_mydata <- round(cdd_mydata, digits=2)
  return(cdd_mydata)
}
cwd <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  cwd_mydata <- climdex.cwd(ci_mydata,spells.can.span.years = FALSE)
  cwd_mydata[is.na(cwd_mydata)] <- 0
  cwd_mydata <- round(cwd_mydata, digits=2)
  return(cwd_mydata)
}
r95ptot <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  r95ptot_mydata <- climdex.r95ptot(ci_mydata)
  r95ptot_mydata <- round(r95ptot_mydata, digits=2)
  return(r95ptot_mydata)
}
r99ptot <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  r99ptot_mydata <- climdex.r99ptot(ci_mydata)
  r99ptot_mydata <- round(r99ptot_mydata, digits=2)
  return(r99ptot_mydata)
}
prcptot <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  prcptot_mydata <- climdex.prcptot(ci_mydata)
  prcptot_mydata <- round(prcptot_mydata, digits=2)
  return(prcptot_mydata)
}
txx <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  txx_mydata <- climdex.txx(ci_mydata,freq = c("annual"))
  txx_mydata <- round(txx_mydata, digits=2)
  return(txx_mydata)
}
tnx <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  tnx_mydata <- climdex.tnx(ci_mydata,freq = c("annual"))
  tnx_mydata <- round(tnx_mydata, digits=2)
  return(tnx_mydata)
}
txn <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  txn_mydata <- climdex.txn(ci_mydata,freq = c("annual"))
  txn_mydata <- round(txn_mydata, digits=2)
  return(txn_mydata)
}
tnn <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  tnn_mydata <- climdex.tnn(ci_mydata,freq = c("annual"))
  tnn_mydata <- round(tnn_mydata, digits=2)
  return(tnn_mydata)
}
tn10p <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  tn10p_mydata <- climdex.tn10p(ci_mydata,freq = c("annual"))
  tn10p_mydata <- round(tn10p_mydata, digits=2)
  return(tn10p_mydata)
}
tx10p <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  tx10p_mydata <- climdex.tx10p(ci_mydata,freq = c("annual"))
  tx10p_mydata <- round(tx10p_mydata, digits=2)
  return(tx10p_mydata)
}
tn90p <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  tn90p_mydata <- climdex.tn90p(ci_mydata,freq = c("annual"))
  tn90p_mydata <- round(tn90p_mydata, digits=2)
  return(tn90p_mydata)
}
tx90p <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  tx90p_mydata <- climdex.tx90p(ci_mydata,freq = c("annual"))
  tx90p_mydata <- round(tx90p_mydata, digits=2)
  return(tx90p_mydata)
}
rx1day <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  rx1day_mydata <- climdex.rx1day(ci_mydata,freq = c("annual"))
  rx1day_mydata <- round(rx1day_mydata, digits=2)
  return(rx1day_mydata)
}
rx5day <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  rx5day_mydata <- climdex.rx5day(ci_mydata,freq = c("annual"))
  #print(rx5day_mydata)
  rx5day_mydata <- round(rx5day_mydata, digits=2)
  return(rx5day_mydata)
}

"""

powerpack = SignatureTranslatedAnonymousPackage(string, "powerpack")


class climatecal(object):

    def __init__(self, stryear,endyear,lat1,lon1,str_date):
        self.stryear = stryear
        self.endyear = endyear
        self.lat1 = lat1
        self.lon1 = lon1
        self.str_date = str_date

    def cal_val(self,var):
        cut_sol = []
        sol = []
        for x in range(self.stryear,self.endyear):
            for y in range(1,13):
                if y<10:
                    # print('csiromk36-rcp45-dd-pr-tas-t2m.'+str(x)+'0'+str(y)+'.nc')
                    # print('csiromk36_rcp85_ps-tas-t2m.'+str(x)+'0'+str(y)+'.nc')
                    m = Dataset('/media/nuyuyii/DATA/CSIRO_MK/RCP85/csiromk36_rcp85_ps-tas-t2m.'+str(x)+'0'+str(y)+'.nc', 'r')
                elif y>=10:
                    m = Dataset('/media/nuyuyii/DATA/CSIRO_MK/RCP85/csiromk36_rcp85_ps-tas-t2m.'+str(x)+str(y)+'.nc', 'r')
                var_name = m.variables[var]
                sol = var_name[:,self.lat1,self.lon1]
                bb = sol.flatten().tolist()
                if var != 'pr':
                    for z in range(0,len(bb)):
                        cut_sol.append(bb[z]-273.15)
                elif var == 'pr':
                    for z in range(0,len(bb)):
                        cut_sol.append(bb[z]*86400)
        c = np.array(cut_sol)
        cut_sol = [float(Decimal("%.2f" % e)) for e in c]

        return cut_sol 

    def date_clim(self):
        pr = self.cal_val('pr') 
        date_climate = powerpack.cal_date(len(pr),str_date)
        return date_climate
 




#result = clim.prcptot()
m = Dataset('/media/nuyuyii/DATA/CSIRO_MK/RCP85/csiromk36_rcp85_ps-tas-t2m.201002.nc', 'r')
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

ind_su =[]
pic = []


eindex=["su","fd","id","tr","gsl","dtr","txx","tnx","txn","tnn","rx1day","rx5day","sdii","r10mm","r20mm","rnnmm","cdd","cwd","r99ptot","prcptot"]
lisYear=range(2006,2007)
eyear=[format(x,'04d') for x in lisYear]

#["2009","2010"]
#["su","fd","id","tr","gsl","wsdi","csdi","dtr","txx","tnx","txn","tnn","tn10p","tx10p","tn90p","tx90p","rx1day","rx5day","sdii","r10mm","r20mm","rnnmm","cdd","cwd","r95ptot","r99ptot","prcptot"]
year=[2006,2007]
str_date = "2005-12-31"

'''
for i in range(0,len(eindex)):
    print(i,"..",eindex[i])

'''
#climdex={}
print(year[0],year[1], len(eindex))
ind = 1

# Note 21499 cdd Na
for x in range(0,len(lats)):#len(lats[0:253])):
    for y in range(0,len(lons)):#len(lons[0:191])):
        o=feature.objects.get(pk=ind)
        clim = climatecal(year[0],year[1],lats[x],lons[y],str_date)
        pr = clim.cal_val('pr')  
        tmax = clim.cal_val('tasmax')
        tmin = clim.cal_val('tasmin')
        value={}
        # res_su
        value[eindex[0]] = powerpack.su(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_fd 
        value[eindex[1]] = powerpack.fd(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_id
        value[eindex[2]] = powerpack.id(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_tr
        value[eindex[3]] = powerpack.tr(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_gsl
        value[eindex[4]] = powerpack.gsl(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_wsdi
       # value[eindex[5]] = powerpack.wsdi(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_csdi 
       # value[eindex[6]] = powerpack.csdi(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_dtr
        value[eindex[5]] = powerpack.dtr(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_txx
        value[eindex[6]] = powerpack.txx(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_tnx
        value[eindex[7]] = powerpack.tnx(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_txn 
        value[eindex[8]] = powerpack.txn(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_tnn 
        value[eindex[9]] = powerpack.tnn(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_tn10p 
       # value[eindex[12]] = powerpack.tn10p(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_tx10p
       # value[eindex[13]] = powerpack.tx10p(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_tn90p
       # value[eindex[14]] = powerpack.tn90p(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_tx90p 
       # value[eindex[15]] = powerpack.tx90p(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_rx1day
        value[eindex[10]] = powerpack.rx1day(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_rx5day 
        value[eindex[11]] = powerpack.rx5day(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_sdii 
        value[eindex[12]] = powerpack.sdii(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_r10mm 
        value[eindex[13]] = powerpack.r10mm(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_r20mm 
        value[eindex[14]] = powerpack.r20mm(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_rnnmm 
        value[eindex[15]] = powerpack.rnnmm(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_cdd 
        value[eindex[16]] = powerpack.cdd(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_cwd 
        value[eindex[17]] = powerpack.cwd(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_r95ptot
       # value[eindex[24]]  = powerpack.r95ptot(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_r99ptot 
        value[eindex[18]] = powerpack.r99ptot(year[0],year[1],len(pr),str_date,tmax,tmin,pr)
        # res_prctot 
        value[eindex[19]] = powerpack.prcptot(year[0],year[1],len(pr),str_date,tmax,tmin,pr)

        #print (o.climdex['su']['2006'])  
        for i in range(0,len(eindex)):
            #print(eyear[0])
            o.climdex[eindex[i]][eyear[0]]={}
            #print (eindex[i],value[eindex[i]][0])  

        #print (o.climdex['su']['2006'])  

        for ey in range(0,len(eyear)):             
            o.climdex[eindex[0]][eyear[ey]] = value[eindex[0]][ey]
            o.climdex[eindex[1]][eyear[ey]] = value[eindex[1]][ey]
            o.climdex[eindex[2]][eyear[ey]] = value[eindex[2]][ey]
            o.climdex[eindex[3]][eyear[ey]] = value[eindex[3]][ey]
            o.climdex[eindex[4]][eyear[ey]] = value[eindex[4]][ey]
            o.climdex[eindex[5]][eyear[ey]] = value[eindex[5]][ey]
            o.climdex[eindex[6]][eyear[ey]] = value[eindex[6]][ey]
            o.climdex[eindex[7]][eyear[ey]] = value[eindex[7]][ey]
            o.climdex[eindex[8]][eyear[ey]] = value[eindex[8]][ey]
            o.climdex[eindex[9]][eyear[ey]] = value[eindex[9]][ey]
            o.climdex[eindex[10]][eyear[ey]] = value[eindex[10]][ey]
            o.climdex[eindex[11]][eyear[ey]] = value[eindex[11]][ey]
            o.climdex[eindex[12]][eyear[ey]] = value[eindex[12]][ey]
            o.climdex[eindex[13]][eyear[ey]] = value[eindex[13]][ey]
            o.climdex[eindex[14]][eyear[ey]] = value[eindex[14]][ey]
            o.climdex[eindex[15]][eyear[ey]] = value[eindex[15]][ey]
            o.climdex[eindex[16]][eyear[ey]] = value[eindex[16]][ey]
            o.climdex[eindex[17]][eyear[ey]] = value[eindex[17]][ey]
            o.climdex[eindex[18]][eyear[ey]] = value[eindex[18]][ey]
            o.climdex[eindex[19]][eyear[ey]] = value[eindex[19]][ey]
        o.save()
        ind=ind+1
    print(lons[y],'--',lats[x],";x ",x,"-y ",y,";ind ",ind)


# pg_dump -D -a -t climate_feature > p85bk.sql
        #ind_su.append([str(year),res_su[0]])
        #pic.append([lons[x],lats[y]])

#coordinate['coor'] = pic

#print(pic)
#out_file = open("index2.json","w")
#json.dump(climdex,out_file)

print('---%s seconds---'%(time.time()-start_time))

#print(cut_res)  







