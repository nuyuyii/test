#csiromk36-rcp45-dd-pr-tas-t2m.200603.nc
import numpy as np
from netCDF4 import Dataset
# import matplotlib.pyplot as plt
import datetime as dt 
from decimal import *
#-------------------Database Psql----------------------
import random, string, psycopg2,time
from string import ascii_lowercase
from random import randint

#-------------------import R---------------------------
import math, datetime
#import rpy2.robjects.lib.ggplot2 as ggplot2
import rpy2.robjects as ro
from rpy2.robjects.packages import importr

importr("climdex.pcic")
importr("PCICt")
#mydata = ro.DataFrame.from_csvfile('/home/thiranan/Project2/ec45indcal.csv')

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
  return(su_mydata)
}

fd <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  fd_mydata <- climdex.fd(ci_mydata)
  
  return(fd_mydata)
}
id <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  id_mydata <- climdex.id(ci_mydata)
  return(id_mydata)
}
tr <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  tr_mydata <- climdex.tr(ci_mydata)
  return(tr_mydata)
}
gsl <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  gsl_mydata <- climdex.gsl(ci_mydata)
  return(gsl_mydata)
}
wsdi <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  wsdi_mydata <- climdex.wsdi(ci_mydata)
  return(wsdi_mydata)
}
csdi <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  csdi_mydata <- climdex.csdi(ci_mydata)
  return(csdi_mydata)
}
dtr <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  dtr_mydata <- climdex.dtr(ci_mydata,freq = c("annual"))
  return(dtr_mydata)
}
sdii <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  sdii_mydata <- climdex.sdii(ci_mydata)
  return(sdii_mydata)
}
r10mm <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  r10mm_mydata <- climdex.r10mm(ci_mydata)
  return(r10mm_mydata)
}
r20mm <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  r20mm_mydata <- climdex.r20mm(ci_mydata)
  return(r20mm_mydata)
}
rnnmm <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  rnnmm_mydata <- climdex.rnnmm(ci_mydata)
  return(rnnmm_mydata)
}
cdd <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  cdd_mydata <- climdex.cdd(ci_mydata)
  return(cdd_mydata)
}
cwd <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  cwd_mydata <- climdex.cwd(ci_mydata,spells.can.span.years = FALSE)
  cwd_mydata[is.na(cwd_mydata)] <- 0
  return(cwd_mydata)
}
r95ptot <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  r95ptot_mydata <- climdex.r95ptot(ci_mydata)
  return(r95ptot_mydata)
}
r99ptot <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  r99ptot_mydata <- climdex.r99ptot(ci_mydata)
  return(r99ptot_mydata)
}
prcptot <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  prcptot_mydata <- climdex.prcptot(ci_mydata)
  return(prcptot_mydata)
}
txx <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  txx_mydata <- climdex.txx(ci_mydata,freq = c("annual"))
  return(txx_mydata)
}
tnx <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  tnx_mydata <- climdex.tnx(ci_mydata,freq = c("annual"))
  return(tnx_mydata)
}
txn <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  txn_mydata <- climdex.txn(ci_mydata,freq = c("annual"))
  return(txn_mydata)
}
tnn <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  tnn_mydata <- climdex.tnn(ci_mydata,freq = c("annual"))
  return(tnn_mydata)
}
tn10p <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  tn10p_mydata <- climdex.tn10p(ci_mydata,freq = c("annual"))
  return(tn10p_mydata)
}
tx10p <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  tx10p_mydata <- climdex.tx10p(ci_mydata,freq = c("annual"))
  return(tx10p_mydata)
}
tn90p <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  tn90p_mydata <- climdex.tn90p(ci_mydata,freq = c("annual"))
  return(tn90p_mydata)
}
tx90p <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  tx90p_mydata <- climdex.tx90p(ci_mydata,freq = c("annual"))
  return(tx90p_mydata)
}
rx1day <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  rx1day_mydata <- climdex.rx1day(ci_mydata,freq = c("annual"))
  return(rx1day_mydata)
}
rx5day <- function(str_year,end_year,numday,str_date,tmax,tmin,pr){
  tmax <- as.numeric(tmax)
  tmin <- as.numeric(tmin)
  pr <- as.numeric(pr)
  ci_mydata <- mdata(str_year,end_year,numday,str_date,tmax,tmin,pr)
  rx5day_mydata <- climdex.rx5day(ci_mydata,freq = c("annual"))
  print(rx5day_mydata)
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
                    m = Dataset('/media/nuyuyii/DATA/CSIRO_MK/RCP45/csiromk36-rcp45-dd-pr-tas-t2m.'+str(x)+'0'+str(y)+'.nc', 'r')
                elif y>=10:
                    m = Dataset('/media/nuyuyii/DATA/CSIRO_MK/RCP45/csiromk36-rcp45-dd-pr-tas-t2m.'+str(x)+str(y)+'.nc', 'r')
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

    def su(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.su(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result


    def txx(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.txx(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def tnx(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.tnx(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def txn(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.txn(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def tnn(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.tnn(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def tn10p(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.tn10p(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def tx10p(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.tx10p(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def tn90p(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.tn90p(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def tx90p(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.tx90p(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def rx1day(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.rx1day(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def rx5day(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.rx5day(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def fd(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.fd(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def id(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.id(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def tr(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.tr(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def gsl(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.gsl(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def wsdi(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.wsdi(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def csdi(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.csdi(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def dtr(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.dtr(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def sdii(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.sdii(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def r10mm(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.r10mm(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def r20mm(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.r20mm(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def rnnmm(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.rnnmm(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def cdd(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.cdd(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def cwd(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.cwd(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def r95ptot(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.r95ptot(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def r99ptot(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.r99ptot(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

    def prcptot(self):
        pr = self.cal_val('pr')  
        tmax = self.cal_val('tasmax')
        tmin = self.cal_val('tasmin')
        result = powerpack.prcptot(self.stryear,self.endyear,len(pr),self.str_date,tmax,tmin,pr)
        return result

 
#--------------------------------------------------------------------------------------------------------

lat1 = 122
lon1 = 222
str_date = "2006-12-31"

'''
#result = clim.prcptot()

m = Dataset('/media/nuyuyii/DATA/CSIRO_MK/RCP45/csiromk36-rcp45-dd-pr-tas-t2m.200701.nc', 'r')
lons = m.variables['lon']
lats = m.variables['lat']
#print(m.variables)
cut_res = []
#print(len(lons[:]))
count = 2502

res_date = []

conn = psycopg2.connect(database="climate",user="postgres",password="198196",host="127.0.0.1", port="5432")
c = conn.cursor()
start_time = time.time()
for x in range(0,len(lons[51:253])):
    for y in range(0,len(lats[51:191])):
        clim = climatecal(2007,2009,lats[y],lons[x],str_date)
        res_date = clim.date_clim()
        res_su = clim.su()
        res_fd = clim.fd()
        res_id = clim.id()
        res_tr = clim.tr()
        res_gsl = clim.gsl()
        res_wsdi = clim.wsdi()
        res_csdi = clim.csdi()
        res_dtr = clim.dtr()

        #cut_res.append(res_su[0])
        #c.execute('INSERT INTO climte_nc(nc_id,year,lon,lat) VALUES (%s, %s, %s, %s)', (count,str(2008),str(lons[x]),str(lats[y])))
        c.execute('INSERT INTO index_table1(c_id,su,fd,id,tr,gsl,wsdi,csdi,dtr) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s)', (count,str(res_su[0]),str(res_fd[0]),str(res_id[0]),str(res_tr[0]),str(res_gsl[0]),str(res_wsdi[0]),str(res_csdi[0]),str(res_dtr[0])))
        count = count+1
    print('id = '+str(count))

conn.commit()

conn.close()
print('---%s seconds---'%(time.time()-start_time))'''

#print(cut_res)  


