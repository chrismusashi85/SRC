
# coding: utf-8

# In[12]:


import math
import numpy as np
import matplotlib.pyplot as plt

'''
44.1kHzのSIN波を48kHzのSIN波にSRCするプログラム

'''
N = 240 # Number of input samples　入力信号のサンプル数
LW = 32 # 畳み込みする関数の長さ（-LW*π/2からLW*π/2まで）
pi = math.pi

Fs_in = 44100
Fs_out = 48000

def hamming(x):
    return 0.54-0.46*math.cos(x)

def sinc(x):
    if x == 0:
        return 1
    else:
        return math.sin(pi*x)/(pi*x)

def windowed_sinc(x):
    return sinc(x)*hamming((x+LW/2)*2*pi/LW)

def convolution(x, m):
    sum = 0
    (dn, n) = math.modf(m * Fs_in/Fs_out)
    for k in range(int(-LW/2), int(LW/2)):
        sum = sum + x[int(n+k)] * windowed_sinc(k-dn)
    return sum
    
y = [] # output
x0 = np.arange(0, 10*2*pi, 2*pi/44.1) # 44.1kHzで10周期分の1khzのSIN波
x1 = np.sin(x0)
x2 = x1.tolist()

'''
x = np.arange(-LW/2, LW/2, 1/10)

y2 = []

for x1 in x:
    y1.append(windowed_sinc(x1))
    y2.append(sinc(x1))

plt.plot(x, y1, label = "y = windowed_sinc(x)")
plt.plot(x, y2, label = "y = sinc(x)")
'''
x = np.arange(N)
x_221 = np.arange(0, 221)

for m1 in range(0, N):
    y.append(convolution(x2, m1))

# input signal
plt.plot(x_221, x1[0:221], marker=".")
    
    
#plt.plot(x, y, marker=".", label="1kHz sin-wave @Fs=48kHz") # 1kHz SIN波 @Fs=48kHz

