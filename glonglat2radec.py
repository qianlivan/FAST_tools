import ephem
import numpy as np
import time
import sys


if (len(sys.argv)<3):
  print 'too few input parameters, format:'
  print 'python glonglat2radec ra dec'
  print 'example:'
  print 'python glonglat2radec 20.0 20.0'
  sys.exit()


glon=ephem.degrees(sys.argv[1])
glat=ephem.degrees(sys.argv[2])

gb=ephem.Galactic(glon,glat,epoch=ephem.J2000)
eb=ephem.Equatorial(gb)
print eb.ra,eb.dec
