import math
import numpy as np
import matplotlib.pyplot as plt

'''
Fs_in[Hz]のSIN波をFs_out[Hz]のSIN波にSRCするプログラム
Fs_in <= Fs_out が条件
'''
LW = 32 # sinc()を畳み込みする長さ（-LW*π/2からLW*π/2まで）
pi = math.pi

Fs_in = 44100 # ここを任意（ただしFs_in <= Fs_out）で変える。入力信号生成部もあわせて修正する。
Fs_out = 48000 # ここを任意で変える

N = Fs_in/100+1 # 入力信号のサンプル数
N_out = int(Fs_out/100) # SRC後信号のサンプル数（1kHzのSin波 10周期分）

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
        if (int(n+k)>=0) and (int(n+k)<N):
            sum = sum + x[int(n+k)] * windowed_sinc(k-dn)
    return sum
    
y = [] # output
# 入力信号生成部
x0 = np.arange(0, 10*2*pi, 2*pi/44.1) # 44.1kHzで10周期分の1khzのSIN波（SRCの入力信号）
x1 = np.sin(x0)
x2 = x1.tolist()

x = np.arange(N_out)

for m1 in range(0, N_out):
    y.append(convolution(x2, m1))

# input signal
#plt.plot(x_221, x1[0:221], marker=".")
    
plt.title("1kHz sin-wave @Fs_out="+str(Fs_out/1000)+"kHz")
plt.plot(x, y, marker=".")
