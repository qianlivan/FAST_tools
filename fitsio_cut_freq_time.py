#!/usr/bin/env python
import numpy as np
import fitsio
import sys
import matplotlib.pyplot as plt
import time
from pylab import *
import os


if (len(sys.argv)<4):
  print 'too few input parameters!'
  print 'example:'
  print 'python fitsio_cut_freq_time.py startchan endchan startn endn FAST.fits'
  startfreq=int(sys.argv[1])
  endfreq=int(sys.argv[2])
  startn=0
  filename=sys.argv[5]
  fits=fitsio.FITS(filename)
  header0 = fits[0].read_header()
  header1 = fits[1].read_header()
  endn=header1['NAXIS2']
  #sys.exit()



startfreq=int(sys.argv[1])
endfreq=int(sys.argv[2])
startn=int(sys.argv[3])
endn=int(sys.argv[4])
filename=sys.argv[5]
outname='output.fits'
fits=fitsio.FITS(filename)


chnum=endfreq-startfreq+1
linenum=endn-startn+1
nrow=linenum



header0 = fits[0].read_header()
header1 = fits[1].read_header()


hdrver=header0['HDRVER']
date=header0['DATE']
ant_x=header0['ANT_X']
ant_y=header0['ANT_Y']
ant_z=header0['ANT_Z']
obsfreq=header0['OBSFREQ']
obsbw=header0['OBSBW']
ra=header0['RA']
dec=header0['DEC']
bmaj=header0['BMAJ']
bmin=header0['BMIN']
date_obs=header0['DATE-OBS']
stt_imjd=header0['STT_IMJD']
stt_smjd=header0['STT_SMJD']
stt_offs=header0['STT_OFFS']
stt_lst=header0['STT_LST']
nchan_origin=header0['OBSNCHAN']
nsblk=header1['NSBLK']
npol=header1['NPOL']
tbin=header1['TBIN']
chan_bw=header1['CHAN_BW']
pol_type=header1['POL_TYPE']

nchan=chnum

obsfreq=((startfreq+endfreq)*1.0/2+1.0)/((nchan-1.0)*1.0/2+1.0)*obsfreq
obsbw=chnum*chan_bw



specs=np.zeros((nrow*nsblk,nchan))
specs_av=np.zeros((nrow,nchan))


command='rm -f '+outname
os.system(command)



data2=fits[1][:]
data3 = np.zeros(nrow,dtype=[('TSUBINT','float64'),('OFFS_SUB','float64'),('LST_SUB','float64'),('RA_SUB','float64'),('DEC_SUB','float64'),('GLON_SUB','float64'),('GLAT_SUB','float64'),('FD_ANG','float32'),('POS_ANG','float32'),('PAR_ANG','float32'),('TEL_AZ','float32'),('TEL_ZEN','float32'),('DAT_FREQ','float32',(nchan)),('DAT_WTS','float32',(nchan)),('DAT_OFFS','float32',(npol*nchan)),('DAT_SCL','float32',(npol*nchan)),('DATA','uint8',(nsblk,npol,nchan,1))])

fitsout=fitsio.FITS(outname,'rw')




#widthfreq=chan_bw
#ch=np.array(range(nchan))
#nu=(ch*1.0/(nchan-1)-0.5)*widthfreq+freq




for index in range(nrow):
    rowindex=index+startn
    data = fits[1].read(rows=[rowindex], columns=['DATA'])
    print index+startn
    for subindex in range(nsblk):
        data3['TSUBINT'][index]=fits[1].read(rows=[rowindex], columns=['TSUBINT'])[0][0]
        data3['OFFS_SUB'][index]=fits[1].read(rows=[rowindex], columns=['OFFS_SUB'])[0][0]
        data3['LST_SUB'][index]=fits[1].read(rows=[rowindex], columns=['LST_SUB'])[0][0]
        data3['RA_SUB'][index]=fits[1].read(rows=[rowindex], columns=['RA_SUB'])[0][0]
        data3['DEC_SUB'][index]=fits[1].read(rows=[rowindex], columns=['DEC_SUB'])[0][0]
        data3['GLON_SUB'][index]=fits[1].read(rows=[rowindex], columns=['GLON_SUB'])[0][0]
        data3['GLAT_SUB'][index]=fits[1].read(rows=[rowindex], columns=['GLAT_SUB'])[0][0]
        data3['FD_ANG'][index]=fits[1].read(rows=[rowindex], columns=['FD_ANG'])[0][0]
        data3['POS_ANG'][index]=fits[1].read(rows=[rowindex], columns=['POS_ANG'])[0][0]
        data3['PAR_ANG'][index]=fits[1].read(rows=[rowindex], columns=['PAR_ANG'])[0][0]
        data3['TEL_AZ'][index]=fits[1].read(rows=[rowindex], columns=['TEL_AZ'])[0][0]
        data3['TEL_ZEN'][index]=fits[1].read(rows=[rowindex], columns=['TEL_ZEN'])[0][0]
        data3['DAT_FREQ'][index]=fits[1].read(rows=[rowindex], columns=['DAT_FREQ'])[0][0][startfreq:endfreq+1]
        data3['DAT_WTS'][index]=fits[1].read(rows=[rowindex], columns=['DAT_WTS'])[0][0][startfreq:endfreq+1]
        
	for ipol in range(npol):
            data3['DAT_OFFS'][index][(ipol-1)*nchan:ipol*nchan]=fits[1].read(rows=[rowindex], columns=['DAT_OFFS'])[0][0][startfreq+(ipol-1)*nchan_origin:endfreq+1+(ipol-1)*nchan_origin]
            data3['DAT_SCL'][index][(ipol-1)*nchan:ipol*nchan]=fits[1].read(rows=[rowindex], columns=['DAT_SCL'])[0][0][startfreq+(ipol-1)*nchan_origin:endfreq+1+(ipol-1)*nchan_origin]
	    tempspec=data[0][0][subindex,ipol,:,0]
            data3['DATA'][index][subindex,ipol,:,0]=tempspec[startfreq:endfreq+1]

fitsout.write(data3,header=header0)
fitsout[0].write_key('HDRVER',hdrver,comment="")
fitsout[0].write_key('FITSTYPE','PSRFITS',comment="FITS definition ")
fitsout[0].write_key('DATE',date,comment="")
fitsout[0].write_key('OBSERVER','FAST_TEAM',comment="Observer name")
fitsout[0].write_key('PROJID','Drift',comment="Project name")
fitsout[0].write_key('TELESCOP','FAST',comment="Telescope name")
fitsout[0].write_key('ANT_X',ant_x,comment="")
fitsout[0].write_key('ANT_Y',ant_y,comment="")
fitsout[0].write_key('ANT_Z',ant_z,comment="")
fitsout[0].write_key('FRONTEND','WIDEBAND',comment="Frontend ID")
fitsout[0].write_key('NRCVR',1,comment="")
fitsout[0].write_key('FD_POLN','LIN',comment="LIN or CIRC")
fitsout[0].write_key('FD_HAND',1,comment="")
fitsout[0].write_key('FD_SANG',0.,comment="")
fitsout[0].write_key('FD_XYPH',0.,comment="")
fitsout[0].write_key('BACKEND','ROACH',comment="Backend ID")
fitsout[0].write_key('BECONFIG','N/A',comment="")
fitsout[0].write_key('BE_PHASE',1,comment="")
fitsout[0].write_key('BE_DCC',0,comment="")
fitsout[0].write_key('BE_DELAY',0.,comment="")
fitsout[0].write_key('TCYCLE',0.,comment="")
fitsout[0].write_key('OBS_MODE','SEARCH',comment="(PSR, CAL, SEARCH)")
fitsout[0].write_key('DATE-OBS',date_obs,comment="Date of observation")
fitsout[0].write_key('OBSFREQ',obsfreq,comment="[MHz] Bandfrequency")
fitsout[0].write_key('OBSBW',obsbw,comment="[MHz] Bandwidth")
fitsout[0].write_key('OBSNCHAN',nchan,comment="Number of channels")
fitsout[0].write_key('CHAN_DM',0.,comment="")
fitsout[0].write_key('SRC_NAME','Drift',comment="Source or scan ID")
fitsout[0].write_key('COORD_MD','J2000',comment="")
fitsout[0].write_key('EQUINOX',2000.,comment="")

fitsout[0].write_key('RA',ra,comment="")
fitsout[0].write_key('DEC',dec,comment="")
fitsout[0].write_key('BMAJ',bmaj,comment="[deg] Beam major axis length")
fitsout[0].write_key('BMIN',bmin,comment="[deg] Beam minor axis length")
fitsout[0].write_key('BPA',0.,comment="[deg] Beam position angle")
fitsout[0].write_key('STT_CRD1','00:00:00.00',comment="")
fitsout[0].write_key('STT_CRD2','00:00:00.00',comment="")
fitsout[0].write_key('TRK_MODE','TRACK',comment="")
fitsout[0].write_key('STP_CRD1','00:00:00.00',comment="")
fitsout[0].write_key('STP_CRD2','00:00:00.00',comment="")
fitsout[0].write_key('SCANLEN',0.,comment="")
fitsout[0].write_key('FD_MODE','FA',comment="")
fitsout[0].write_key('FA_REQ',0.,comment="")
fitsout[0].write_key('CAL_MODE','OFF',comment="")
fitsout[0].write_key('CAL_FREQ',0.,comment="")
fitsout[0].write_key('CAL_DCYC',0.,comment="")
fitsout[0].write_key('CAL_PHS',0.,comment="")
fitsout[0].write_key('STT_IMJD',stt_imjd,comment="Start MJD (UTC days) (J - long integer)")
fitsout[0].write_key('STT_SMJD',stt_smjd,comment="[s] Start time (sec past UTC 00h) (J)")
fitsout[0].write_key('STT_OFFS',stt_offs,comment="[s] Start time offset (D)")
fitsout[0].write_key('STT_LST',stt_lst,comment="[s] Start LST (D)")

fitsout[1].write_key('INT_TYPE','TIME',comment="Time axis (TIME, BINPHSPERI, BINLNGASC, etc)")
fitsout[1].write_key('INT_UNIT','SEC',comment="Unit of time axis (SEC, PHS (0-1),DEG)")
fitsout[1].write_key('SCALE','FluxDen',comment="")
fitsout[1].write_key('NPOL',1,comment="Nr of polarisations")
fitsout[1].write_key('POL_TYPE',pol_type,comment="Polarisation identifier")
fitsout[1].write_key('TBIN',tbin,comment="[s] Time per bin or sample")
fitsout[1].write_key('NBIN',1,comment="")
fitsout[1].write_key('NBIN_PRD',0,comment="Nr of bins/pulse period (for gated data)")
fitsout[1].write_key('PHS_OFFS',0.0,comment="Phase offset of bin 0 for gated data")
fitsout[1].write_key('NBITS',8,comment="Nr of bits/datum ")
fitsout[1].write_key('NSUBOFFS',0,comment="Subint offset ")
fitsout[1].write_key('NCHNOFFS',0,comment="Channel/sub-band offset for split files")
fitsout[1].write_key('NCHAN',nchan,comment="Number of channels")
fitsout[1].write_key('CHAN_BW',chan_bw,comment="[MHz] Channel/sub-band width")
fitsout[1].write_key('NSBLK',nsblk,comment="Samples/row ")
fitsout[1].write_key('EXTNAME','SUBINT  ',comment="name of this binary table extension")
fitsout[1].write_key('EXTVER',1,comment="")
fitsout.close()

