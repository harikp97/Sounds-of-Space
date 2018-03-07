#!/usr/bin/python
"""
Created on Sun Sep  3 02:15:09 2017

@author: Harikrishnan
"""
import numpy as np
from scipy.io import wavfile

def write_wavfile(filename,fs,data):
	d = np.int16(data/np.max(np.abs(data)) * 32767 * 0.9)
	wavfile.write(filename,int(fs), d)

def reqshift(data,fshift=1000,sample_rate=10):
	x = np.fft.rfft(data)
	T = len(data)/float(sample_rate)
	df = 1.0/T
	nbins = int(fshift/df)
	# print T,df,nbins,x.real.shape
	y = np.roll(x.real,nbins) + 1j*np.roll(x.imag,nbins)
	z = np.fft.irfft(y)
	return z
def star_walk():
	i=0
	a=np.array([['Sirius','A',6.75],
		   ['Canopus','F',6.4],
		   ['Rigil','G',14.67],
		   ['Arcturus','K',14.27],
		   ['Vega','A',18.62],
		   ['Capella','G',5.28],
		   ['Rigel','B',5.25],
		   ['Procyon','F',7.65],
		   ['Betelgeuse','M',5.92],
		   ['Achernar','B',1.63],
		   ['Hadar','B',14.07],
		   ['Altair','A',19.85],
		   ['Acrux','B',12.45],
		   ['Aldebaran','K',4.6],
		   ['Spica','B',13.41],
		   ['Antares','M',16.48],
		   ['Pollux','K',7.75],
		   ['Fomalhault','A',22.97],
		   ['Deneb','A',20.68],
		   ['Mimosa','B',12.8],
		   ['Regulus','B',10.13],
		   ['Adhara','B',6.98],
		   ['Castor','A',7.58],
		   ['Gacrux','M',12.52],
		   ['Shaula','B',17.57],
		   ['Bellatrix','B',5.42],
		   ['Elnath','B',5.43],
		   ['Miaplacidus','A',9.22],
		   ['Alnilam','B',5.6],
		   ['Alnair','B',22.13],
		   ['Alnitak','O',5.68],
		   ['Regor','O',8.17],
		   ['Alioth','A',12.9],
		   ['Kaus Aust','B',18.4],
		   ['Mirfak','F',3.4],
		   ['Dubhe','K',11.07],
		   ['Wezen','F',7.13],
		   ['Alkaid','B',13.8],
		   ['Sargas','F',17.62],
		   ['Avior','K',8.38],
		   ['Menkalinan','A',6.00],
		   ['Atria','K',16.82],
		   ['Koo She','A',8.75],
		   ['Alhena','A',6.63],
		   ['Peacock','B',20.43],
		   ['Polaris','F',2.53],
		   ['Mirzam','B',6.38],
		   ['Alphard','K',9.47],
		   ['Algieba','K',10.33],
		   ['Hamal','K',2.12]])
	b=np.zeros(a.shape[0])
	for i in range(0,a.shape[0],1):
		b[i]=float(a[i][2])

	a=a[b.argsort()]
	b=np.sort(b)
	s=np.zeros(1)
	f=0
	for i in range(0,b.size-1,1):
		if(a[i][1]=='O'):
			f=450
		elif(a[i][1]=='B'):
			f=400
		elif(a[i][1]=='A'):
			f=360
		elif(a[i][1]=='F'):
			f=320
		elif(a[i][1]=='G'):
			f=300
		elif(a[i][1]=='K'):
			f=270
		elif(a[i][1]=='M'):
			f=240

		x=np.zeros(480)
		x[f]=10
		y=np.fft.irfft(x)
		s=np.concatenate((s,y),axis=0)
	
	write_wavfile("50stars.wav",4096,s)     
