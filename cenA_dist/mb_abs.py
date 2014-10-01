import numpy as np
import matplotlib.pyplot as plt
import sys

from scipy.interpolate import interp1d



def interp_mb():
	s1=np.loadtxt('../ni_logbol_c00.txt', usecols=(1, 3))
	s1[:,1]=pow(10, s1[:,1])
	s1[:,1]/=1e43
	s1[:,0]=abs(s1[:,0])
	s1=s1[s1[:,1].argsort()]  
	lbol=s1[:,1]
	lbol=np.delete(lbol, 2)
	mb=np.delete(s1[:,0], 2)
	gl=interp1d(lbol,mb , kind='cubic')
	l=np.linspace(lbol.min(), lbol.max())
	spl=gl(l)
	tl=float(sys.argv[1])
	pf=np.polyfit(lbol, mb, 2)
	bf=pf[0]*tl**2+pf[1]*tl+pf[2]
	print bf
	plt.plot(lbol, mb, 'r+')
	plt.show()
	l1=abs(l-tl)
	print spl[l1==min(l1)]
	
if len(sys.argv)==2:	
	interp_mb()
else:
	