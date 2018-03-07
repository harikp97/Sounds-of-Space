import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Defining constants

#Air Density
rho=1.225
g=9.8
#Draf Coefficient
cd=0.75
#Exhaust Velocity
ue=3000
#Frontal reference area
a=10
#Fuel mass flow rate
mdot=5000
#Rocket initial mass
mass=300000

iterations = 10000

h=np.zeros(1)
v=np.zeros(1)
m=np.zeros(1)
m[0]=mass
v[0]=60

#for i in range(0,iterations-1,1):
#	if(m[i]>50000):
#		m[i+1] = m[i] + (-1*mdot) * 0.1
#	else:
#		m[i+1]=m[i]
#		mdot=0
#		ue=0
#	h[i+1] = h[i] + v[i] * 0.1
#	v[i+1] = v[i] + (-1*g - 0.5*rho*v[i]*np.abs(v[i])*cd*a/m[i] + v[i]*mdot*ue/(np.abs(v[i])*m[i])) * 0.1

i=0
while (h[i]>=0):
	if(m[i]>50000):
		m = np.insert(m,i+1,m[i] + (-1*mdot) * 0.1)
	else:
		m = np.insert(m,i+1,m[i])
		mdot=0
		ue=0
	h = np.insert(h,i+1,h[i] + v[i] * 0.1)
	v = np.insert(v,i+1,v[i] + (-1*g - 0.5*rho*v[i]*np.abs(v[i])*cd*a/m[i] + v[i]*mdot*ue/(np.abs(v[i])*m[i])) * 0.1)
	
	i=i+1

def write_wavfile(filename,fs,data):
	d = np.int16(data/np.max(np.abs(data)) * 32767 * 0.9)
	wavfile.write(filename,int(fs), d)
	

def plot():
	t=np.arange(0,h.size,1)
	plt.figure()
	plt.xlabel('Time')
	plt.ylabel('Height')
	plt.plot(t*0.1,h)

	plt.figure()
	plt.xlabel('Time')
	plt.ylabel('Velocity')
	plt.plot(t*0.1,v)

	plt.figure()
	plt.xlabel('Time')
	plt.ylabel('Mass')
	plt.plot(t*0.1,m)
	plt.show()

def sound():
	v_abs=np.abs(v)
	vmin=np.min(v_abs)
	vmax=np.max(v_abs)
	smin=240
	smax=480
	sh=(smax-smin)/(vmax-vmin)
	for i in range(v_abs.shape[0]):
		v_abs[i]=(v_abs[i]-vmin)*sh + smin

	s=np.zeros(1)
	for i in range(v_abs.size):
		if(v_abs[i]<270):
			f=240
		elif(v_abs[i]<300):
			f=270
		elif(v_abs[i]<320):
			f=300
		elif(v_abs[i]<360):
			f=320
		elif(v_abs[i]<400):
			f=360
		elif(v_abs[i]<450):
			f=400	
		else:
			f=450
		x=np.zeros(480)
		x[f]=1000*(h[i]+1)
		#x[f]=np.exp(-1*radius[i]) * 100
		y=np.fft.irfft(x)
		s=np.concatenate((s,y),axis=0)	
		
	print(s.size)
	write_wavfile("sound2",40960,s)
