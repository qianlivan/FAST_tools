import numpy as np
import ephem
import sys

#------------------------------------------------------------------
# Written by Lei QIAN
# created on 20260318
# version 20260318
# provide current right acsension (ra) declination (dec),
# calculate the ra, dec of the beams
# Usage:
#
# Example:
#
#------------------------------------------------------------------

if (len(sys.argv)<3):
  print('too few input parameters, format:')
  print('python snapshotplan2.py ra dec')
  print('                   (degrees)')
  print('example:')
  print('python snapshotplan2.py 20:00:00 20:00:00')
  #sys.exit()
  ra0=ephem.hours('20:00:00')
  dec0=ephem.degrees('20:00:00')
  ang= 23.4
elif (len(sys.argv)==3):
  ang = 23.4
else:
  ra0=ephem.hours(sys.argv[1])
  dec0=ephem.degrees(sys.argv[2])
  ang=float(sys.argv[3])

def d2d(dec):
    if(dec<0):
        dec=np.abs(dec)
        decd = int(dec)
        decm = int((dec-decd)*60)
        decs = (dec-decd-decm/60.0)*3600

        if (decd<10):
           strdecd=str(0)+str(decd)
        else:
           strdecd=str(decd)
        if (decm<10):
           strdecm=str(0)+str(decm)
        else:
           strdecm=str(decm)

        strdecs=str(decs)

        #decstr=str(decd)+':'+str(decm)+':'+str(decs)
        decstr='-'+strdecd+':'+strdecm+':'+strdecs
    else:
        decd = int(dec)
        decm = int((dec-decd)*60)
        decs = (dec-decd-decm/60.0)*3600

        if (decd<10):
           strdecd=str(0)+str(decd)
        else:
           strdecd=str(decd)
        if (decm<10):
           strdecm=str(0)+str(decm)
        else:
           strdecm=str(decm)

        strdecs=str(decs)

        #decstr=str(decd)+':'+str(decm)+':'+str(decs)
        decstr='+'+strdecd+':'+strdecm+':'+strdecs

    return decstr
print('current: ', ra0,dec0)

def d2h(ra):
    ra_deg = ra % 360.0
    #rah = int(ra/15)
    #ram = int((ra-rah*15)*60/15)
    #ras = (ra-rah*15-ram*15/60.0)*3600/15
    #if (rah<10):
    #   strrah=str(0)+str(rah)
    #else:
    #   strrah=str(rah)
    #if (ram<10):
    #   strram=str(0)+str(ram)
    #else:
    #   strram=str(ram)

    #strras=str(ras)

    #rastr=strrah+':'+strram+':'+strras
    #return rastr

    h = ra_deg / 15.0
    hh = int(h)
    mm = int((h - hh) * 60.0)
    ss = ((h - hh) * 60.0 - mm) * 60.0
    return f"{hh:02d}:{mm:02d}:{ss:07.4f}"

distance=5.74
print('M02')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+5.74/60.0*np.cos(ang/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang3=ang-60.0
distance=5.74
print('M03')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang3/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang3/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang3/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang4=ang-120.0
distance=5.74
print('M04')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang4/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang4/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang4/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang5=ang-180.0
distance=5.74
print('M05')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang5/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang5/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang5/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang6=ang+120.0
distance=5.74
print('M06')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang6/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang6/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang6/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang7=ang+60.0
distance=5.74
print('M07')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang7/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang7/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang7/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang8=ang
distance=5.74*2
print('M08')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang8/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang8/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang8/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)


ang9=ang-30.0
distance=5.74*np.sqrt(3)/2*2
print('M09')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang9/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang9/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang9/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang10=ang-60.0
distance=5.74*2
print('M10')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang10/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang10/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang10/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang11=ang-90.0
distance=5.74*np.sqrt(3)/2*2
print('M11')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang11/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang11/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang11/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang12=ang-120.0
distance=5.74*2
print('M12')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang12/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang12/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang12/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang13=ang-150.0
distance=5.74*np.sqrt(3)/2*2
print('M13')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang13/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang13/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang13/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang14=ang-180.0
distance=5.74*2
print('M14')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang14/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang14/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang14/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang15=ang+150.0
distance=5.74*np.sqrt(3)/2*2
print('M15')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang15/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang15/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang15/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang16=ang+120.0
distance=5.74*2
print('M16')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang16/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang16/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang16/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang17=ang+90.0
distance=5.74*np.sqrt(3)/2*2
print('M17')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang17/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang17/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang17/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)

ang18=ang+60.0
distance=5.74*2
print('M18')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang18/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang18/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang18/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)


ang19=ang+30.0
distance=5.74*np.sqrt(3)/2*2
print('M19')
#ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang19/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))/180.0*np.pi))
ra0_new=d2h(float(ephem.hours(ra0))*180.0/np.pi+distance/60.0*np.cos(ang19/180.0*np.pi)/np.cos(float(ephem.degrees(dec0))))
dec0_new=d2d(float(ephem.degrees(dec0))*180.0/np.pi+distance/60.0*np.sin(ang19/180.0*np.pi))
#print(ra0_new,float(ephem.hours(ra0_new))*180.0/np.pi*60,dec0_new,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
print(ra0_new,dec0_new)
print(float(ephem.hours(ra0_new))*180.0/np.pi*60,float(ephem.degrees(dec0_new))*180.0/np.pi*60)
