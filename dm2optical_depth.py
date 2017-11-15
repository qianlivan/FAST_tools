import sys

if (len(sys.argv)<2):
  print 'too few inputs!'
  print 'Usage:'
  print 'python dm2optical_depth.py dm'
  print 'example:'
  print 'python dm2optical_depth.py 30.0'
  sys.exit()

dm=float(sys.argv[1])

sigmaT=6.65e-29*1.0e4*3.08567758149137e18

print 'tau: ',dm*sigmaT
