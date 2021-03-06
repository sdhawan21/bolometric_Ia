import numpy as np
import matplotlib.pyplot as plt
import easygui as eg
import sys

from scipy.interpolate import interp1d
band=sys.argv[1]
tmax=56689.7
def spl_fit(band):
	lc=np.loadtxt('lc2fit_'+band+'.dat', skiprows=8)
	ph=lc[:,0]-tmax
	plt.plot(ph, lc[:,1])
	nsamp=100
	a=eg.multchoicebox("choose from range:", "choices", ph)
	t_arr=[]
	
	cond=(ph>float(a[0])) & (ph<float(a[1]))
	ph1=ph[cond]
	print a
	for k in range(nsamp):
		real=np.random.normal(lc[:,1][cond], lc[:,2][cond])
		ter=interp1d(ph[cond], real, kind='cubic')
		l=np.linspace(ph1.min(), ph1.max())
		kk=ter(l)
		t=l[kk==min(kk)]
		t_arr.append(t[0])
	return np.array(t_arr)	
def main():
	t_arr=spl_fit(band)
	return np.mean(t_arr), np.std(t_arr)
print main()
