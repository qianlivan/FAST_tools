import ephem
import numpy as np
import time
import sys

if(len(sys.argv)<4):
  print 'too few input parameters, format:'
  print 'python j2000tojnow.py ra dec mjd'
  print 'example:'
  print 'python j2000tojnow.py 20:00:00 20:00:00 58000'
  sys.exit()

 

convert=np.pi/180.0
 

ra0=ephem.degrees(ephem.hours(sys.argv[1]))
dec0=ephem.degrees(sys.argv[2])
mjd=float(sys.argv[3])

jd=mjd+2400000.5
date=ephem.julian_date('1899/12/31 12:00:00')
djd=jd-date

epoch_date=ephem.Date(djd)


#new = ephem.Equatorial(ra0, dec0, epoch=ephem.now())
new = ephem.Equatorial(ra0, dec0, epoch=ephem.J2000)
old = ephem.Equatorial(new, epoch=epoch_date)
print('%s %s'%(new.ra,new.dec))
print new.ra/convert,new.dec/convert
print('%s %s'%(old.ra,old.dec))
print old.ra/convert,old.dec/convert

