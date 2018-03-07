# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:22:47 2017

@author: Harikrishnan
"""

import numpy as np
import template
from scipy.io import wavfile

def write_wavfile(filename,fs,data):
    d = np.int16(data/np.max(np.abs(data)) * 32767 * 0.9)
    wavfile.write(filename,int(fs), d)
    
def reqshift(data,fshift=400,sample_rate=4096):
    x = np.fft.rfft(data)
    T = len(data)/float(sample_rate)
    df = 1.0/T
    nbins = int(fshift/df)
    # print T,df,nbins,x.real.shape
    y = np.roll(x.real,nbins) + 1j*np.roll(x.imag,nbins)
    z = np.fft.irfft(y)
    return z

def sound(m1,m2,fs=4096,shift=400,t=2):
    t_f,t_freq = template.createTemplate(fs,t,m1,m2)
    t_f[t_freq<25]=0
    data=np.fft.irfft(t_f)
    data=reqshift(data,shift,fs)
    write_wavfile("{0}-{1}_shift={2}.wav".format(m1,m2,shift),fs,data)