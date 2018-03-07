import numpy as np
from random import *
from scipy.io import wavfile

def write_wavfile(filename,fs,data):
	d = np.int16(data/np.max(np.abs(data)) * 32767 * 0.9)
	wavfile.write(filename,int(fs), d)

# Number of pulsars under consideration
n=20

# Initialize random periods and distances for pulsars
periods=np.zeros(n)
inv_distances=np.zeros(n)
# Periods
for i in range(0,n,1):
	periods[i]=randint(1,100)

# Frequencies
freq = 1/periods
# Shifting frequencies to discrete notes
fmax = np.max(freq)
fmin = np.min(freq)
smax = 480
smin = 240
sh = (smax-smin)/(fmax-fmin)
for i in range(freq.shape[0]):
	freq[i]=(freq[i]-fmin)*sh + smin
	if(freq[i]<270):
		freq[i]=240
	elif(freq[i]<300):
		freq[i]=270
	elif(freq[i]<320):
		freq[i]=300
	elif(freq[i]<360):
		freq[i]=320
	elif(freq[i]<400):
		freq[i]=360
	elif(freq[i]<450):
		freq[i]=400	
	else:
		freq[i]=450

# Distances
for i in range(0,n,1):
	inv_distances[i]=uniform(1,100)

s=np.zeros(1)

for j in range(1,1000,1):
	x=np.zeros(480)
	for i in range(0,n,1):
		if(j%periods[i]==0):
			x[freq[i]]=x[freq[i]] + inv_distances[i]
	
	y=np.fft.irfft(x)
	s=np.concatenate((s,y),axis=0)

print(s.size)
write_wavfile("n=20",4096,s)
		
