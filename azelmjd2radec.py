import ephem
import numpy as np
import time
import sys

if (len(sys.argv)<4):
  print 'too few input parameters, format:'
  print 'python azel2radec.py az el delta_T(seconds)'
  print 'example:'
  print 'python azel2radec.py 20.0 20.0 10'
  #sys.exit()
  print 'default values used'
  az0=ephem.degrees(20.0)
  el0=ephem.degrees(20.0)
  mjd=np.float(10)
else:
  az0=ephem.degrees(sys.argv[1])
  el0=ephem.degrees(sys.argv[2])
  mjd=np.float(sys.argv[3])



convert=np.pi/180.0

class coordinate:
      def __init__(place):
          place.name=''
          place.ra=''
          place.dec=''
          place.alt=''

Dawodang=coordinate()
Dawodang.name='Dawodang'
Dawodang.lon=str(106.856666872)  # Official parameter
Dawodang.lat=str(25.6529518158)  # Official parameter

def localtoec(az,el,mjd):
    global convert
    getlocal = ephem.Observer()
    getlocal.lon = Dawodang.lon
    getlocal.lat = Dawodang.lat
    getlocal.elevation = 1110.028801 # altitude
    getlocal.temp = 25
    getlocal.pressure = 1.01325e3
    getlocal.epoch = ephem.J2000
    #ct = time.gmtime(time.time()+delta_T)
    #ct3 = time.strftime("%Y/%m/%d %H:%M:%S",ct)
    jd=mjd+2400000.5
    date=ephem.julian_date('1899/12/31 12:00:00')
    djd=jd-date
    ct3=ephem.Date(djd)
    print ct3
    getlocal.date = ct3 # UT
    ra,dec = getlocal.radec_of(az,el)
    return ra,dec


ra,dec=localtoec(az0,el0,mjd)
print ra,dec                                # ra in h m s  dec in d m s
