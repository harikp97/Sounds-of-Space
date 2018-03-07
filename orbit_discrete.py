from __future__ import print_function, division
import numpy as np
from PyAstronomy import pyasl
import matplotlib.pylab as plt
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


def orbit():
	# Instantiate a Keplerian elliptical orbit with
	# semi-major axis of __ length units,
	# a period of __ time units, eccentricity of __,
	# longitude of ascending node of __ degrees, an inclination
	# of __ deg, and a periapsis argument of __ deg.
	ke = pyasl.KeplerEllipse(1.3, 10., e=0.9, Omega=70., i=10.0, w=110.0)

	# Get a time axis
	t = np.linspace(0, 20, 100)

	# Calculate the orbit position at the given points
	# in a Cartesian coordinate system.
	pos = ke.xyzPos(t)
	#print("Shape of output array: ", pos.shape)

	# x, y, and z coordinates for 50th time point
	#print("x, y, z for 50th point: ", pos[50, ::])

	# Calculate orbit radius
	radius = ke.radius(t)
	
	# Calculate velocity on orbit
	vel = ke.xyzVel(t)
	# Find the nodes of the orbit (Observer at -z)
	ascn, descn = ke.xyzNodes_LOSZ()
	
	velocity=np.zeros(vel.shape[0])
	for i in range(vel.shape[0]):
		velocity[i]=velocity[i] + (vel[i][0]**2 + vel[i][1]**2 + vel[i][2]**2)**(0.5)
	print(velocity.size)
	vmin=velocity.min()
	vmax=velocity.max()
	
	#Freq Shift
	smax=480
	smin=240
	if(vmax-vmin<0.001):
		sh=0
	else:
		sh=(smax-smin)/(vmax-vmin)	
	for i in range(velocity.shape[0]):
		velocity[i]=(velocity[i]-vmin)*sh + smin
		
	s=np.zeros(1)
	for i in range(velocity.size):
		if(velocity[i]<270):
			f=240
		elif(velocity[i]<300):
			f=270
		elif(velocity[i]<320):
			f=300
		elif(velocity[i]<360):
			f=320
		elif(velocity[i]<400):
			f=360
		elif(velocity[i]<450):
			f=400	
		else:
			f=450
		#print(f)
		x=np.zeros(480)
		#x[f]=20/radius[i]
		x[f]=np.exp(-1*radius[i]) * 100
		y=np.fft.irfft(x)
		s=np.concatenate((s,y),axis=0)		
	
	print(s.size)
	write_wavfile("e=0.9_exp.wav",4096,s)
	#write_wavfile("e=0.9_inverse.wav",4096,s)
