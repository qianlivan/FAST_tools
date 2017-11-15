import ephem
import numpy as np
import time
import sys

if (len(sys.argv)<3):
  print 'too few input parameters, format:'
  print 'python radec2azel.py ra    dec'
  print '                     (hours) (degrees)'
  print 'example:'
  print 'python radec2azel.py 20:00:00 20:00:00'
  sys.exit()


convert=np.pi/180.0

class coordinate:
      def __init__(place):
          place.name=''
          place.lon=''
          place.lat=''

Dawodang=coordinate()
Dawodang.name='Dawodang'
Dawodang.lon=str(106.856666872)  # Official parameter
Dawodang.lat=str(25.6529518158)  # Official parameter

def ectolocal(ra,dec,mjd):
    global convert
    getlocal = ephem.Observer()
    getlocal.lon = Dawodang.lon
    getlocal.lat = Dawodang.lat
    getlocal.elevation = 1110.028801 # altitude
    getlocal.temp = 25
    getlocal.pressure = 0
    #ct = time.gmtime()            # local time
    #ct3 = time.strftime("%Y/%m/%d %H:%M:%S",ct)
    jd=mjd+2400000.5
    date=ephem.julian_date('1899/12/31 12:00:00')
    djd=jd-date
    ct3=ephem.Date(djd)
    getlocal.date = ct3           # UT
    print 'UT: ',ct3
    body = ephem.FixedBody()
    body._ra = ra                 # input right ascension
    body._dec = dec               # input declination
    body._epoch = ephem.J2000
    body.compute(getlocal)
    x= float(body.az)*180/np.pi   # convert radian to degree
    y= float(body.alt)*180/np.pi  # convert radian to degree
    return x,y


ra0=ephem.hours(sys.argv[1])
dec0=ephem.degrees(sys.argv[2])
mjd=ephem.degrees(sys.argv[3])
az,el=ectolocal(ra0,dec0,mjd)
print 'Az                El'
print az,el                       # output azimuthal and elevation
