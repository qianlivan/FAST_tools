import numpy as np
import ephem
import sys
import urllib
import urllib2

if (len(sys.argv)<4):
#if (len(sys.argv)<2):
  print 'too few inputs!'
  print 'example:'
  print 'python dm2distance.py 04:00:00 20:00:00 30.0'
  sys.exit()

ra=ephem.hours(sys.argv[1])
dec=ephem.degrees(sys.argv[2])
dm=float(sys.argv[3])


eb=ephem.Equatorial(ra,dec,epoch=ephem.J2000)
gb=ephem.Galactic(eb)
#print gb.lon, gb.lat

glong= float(ephem.degrees(gb.lon))*180.0/np.pi  
glat=float(ephem.degrees(gb.lat))*180.0/np.pi
#print glong,glat


urlstr="http://119.78.162.254/dmodel/index.php?mode=Gal&gl="+str('%.2f'% glong)+"&gb="+str('%.2f'% glat)+"&dm="+str(dm)+"&DM_Host=&ndir=1"
response = urllib2.urlopen(urlstr)

data = response.read()

data1=data.split('Dist:')[2]
dist=data1.split('log(tau_sc): ')[0]
print float(dist),'pc'
