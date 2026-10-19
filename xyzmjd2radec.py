import ephem
import numpy as np
import time
import sys

# (x,y,z) is the coordinate in the FAST coordinate system,
# (0,0,0) is at the origin of the shpere of the reflector.
# You need (x,y,z) and the time (here is MJD) to convert to (ra, dec).
# Note that MJD is UTC.
# The start point of MJD is 1858-11-17 00:00:00 UT.
# MJD = JD - 2,400,000.5
# The star point of JD is BCE 4713-1-1 12:00:00 UT.
#


if (len(sys.argv)<5):
  print('too few input parameters, format:')
  print('python xyzmjd2radec.py x y z mjd')
  print('example:')
  print('python xyzmjd2radec.py 80.0 90.0 -155.0 58000')
  #sys.exit()
  x0 = 80.0
  y0 = 90.0
  z0 = -155.0
  mjd = 50000
  print('Default values used.')
  print(' ')
else:
  x0 = float(sys.argv[1])
  y0 = float(sys.argv[2])
  z0 = float(sys.argv[3])
  mjd = float(sys.argv[4])



convert=np.pi/180.0

class coordinate:
      def __init__(place):
          place.name=''
          place.ra=''
          place.dec=''
          place.alt=''

Dawodang=coordinate()
Dawodang.name='Dawodang'
#Dawodang.ra='106.856594'
#Dawodang.dec='25.652939'
#Dawodang.ra=str(106.85645657571428)
#Dawodang.dec=str(25.6534387)
Dawodang.ra=str(106.856666872)  # Official parameter of latitude
Dawodang.dec=str(25.6529518158) # Official parameter of longitude
Dawodang.alt=str(1138.72178)    # Official parameter of altitude

def localtoec(az,el,mjd):
    global convert
    getlocal = ephem.Observer()
    getlocal.long, getlocal.lat = Dawodang.ra,Dawodang.dec # Geographic latitude and longitude at Dawodang
    getlocal.pressure = 0
    getlocal.epoch = ephem.J2000
    #ct = time.gmtime()         # Current time
    #ct3 = time.strftime("%Y/%m/%d %H:%M:%S",ct)
    jd=mjd+2400000.5
    date=ephem.julian_date('1899/12/31 12:00:00')
    djd=jd-date
    ct3=ephem.Date(djd)
    #print ct3
    getlocal.date = ct3 # UT

    # crab
    #FAST=ephem.Observer()
    #FAST.lat='25.652939'
    #FAST.lon='106.856594'
    #FAST.horizon='-18' # Astronomical twilight uses the value -18 degrees
    #body = ephem.FixedBody()
    #ra0=ephem.hours('05:34:32.0')
    #dec0=ephem.degrees('+22:01:10')
    #body._ra = ra0
    #body._dec = dec0
    #body._epoch = ephem.J2000
    #ttrans=FAST.next_transit(body)
    #print ttrans
    #getlocal.date = ttrans # UT

    ra,dec = getlocal.radec_of(az*convert,el*convert)
    return ra,dec

#x0 = float(sys.argv[1])
#y0 = float(sys.argv[2])
#z0 = float(sys.argv[3])
#R = 300*(1.0-0.4665)
#R = 300*(1.0-0.4611)
R=np.sqrt(x0**2+y0**2+z0**2)
# Convert from the coordinate pointing downward to a coordinate pointing upward.
z=-z0
y=-x0
x=-y0


az0 = 0.0

# Deal with the degeneration.
if (np.abs(x) < 1.0-8):
   if (y>0):
      az0 = 90.0
   else:
      az0 = 270.0
else:
   tempaz0 = np.arctan(y/x)/convert
   if (x>0 and y>0):
      az0 = tempaz0
   if ((x>0 and y<0) or (x>0 and y==0)):
       az0 = tempaz0+360.0
   if (x<0 and y>0):
       az0 = tempaz0+180.0
   if ((x<0 and y<0) or (x<0 and y==0)):
       az0 = tempaz0+180.0
el0 = np.arcsin(z/R)/convert
print(az0,el0)
print(float(az0)/convert,float(el0)/convert)
print(ephem.degrees(az0)/convert,ephem.degrees(el0)/convert)


# Output the coordinate in nearly realtime.
'''
while 1:
    ra,dec=localtoec(az0,el0)
    print ephem.hours(ra),ephem.degrees(dec)
    print ephem.degrees(ra)/convert,ephem.degrees(dec)/convert
    time.sleep(0.5)
'''

ra,dec=localtoec(az0,el0,mjd)
print("RA       Dec")
print(ra,dec)                               # Output of RA(J2000) hh:mm:ss and Dec(J2000) dd:mm:ss
print(float(ra)/convert,float(dec)/convert) # Output of RA(J2000) and Dec(J2000) in degrees
#print ephem.degrees(ra)/convert,ephem.degrees(dec)/convert
