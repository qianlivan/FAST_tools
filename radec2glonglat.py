import ephem
import numpy as np
import time
import sys


if (len(sys.argv)<3):
  print 'too few input parameters, format:'
  print 'python radec2glonglat.py ra dec'
  print '                     (hours) (degrees)'
  print 'example:'
  print 'python radec2glonglat.py 20:00:00 20:00:00'
  sys.exit()


ra0=ephem.hours(sys.argv[1])
dec0=ephem.degrees(sys.argv[2])

eb=ephem.Equatorial(ra0,dec0,epoch=ephem.J2000)
gb=ephem.Galactic(eb)
print gb.lon, gb.lat
print '%.2f %.2f' % (float(ephem.degrees(gb.lon))*180.0/np.pi,  float(ephem.degrees(gb.lat))*180.0/np.pi)
