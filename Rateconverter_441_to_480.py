
import math
import numpy as np
import matplotlib.pyplot as plt
import wave
from scipy import fromstring, int16
import struct

# ==== file open ====
fname_r = r'C:\Low_44100.wav'
fname_w = r'C:\Low_48000_tmp.wav'

waveFile_r = wave.open(fname_r, mode='rb')
waveFile_w = wave.open(fname_w, mode='wb')

# チャネル数：monoなら1, stereoなら2
nchannles = waveFile_r.getnchannels()
# 音声データ1サンプルあたりのバイト数。2なら2bytes(16bit)
samplewidth = waveFile_r.getsampwidth()
# サンプリング周波数
framerate = waveFile_r.getframerate()
# 音声のデータ点の数
nframes = waveFile_r.getnframes()
print("Channel num : ", nchannles)
print("Sample width : ", samplewidth)
print("Sampling rate : ", framerate)
print("Frame num : ", nframes)
data = waveFile_r.readframes(nframes)
num_data = fromstring(data, dtype = int16)
left_data = num_data[::2]
right_data = num_data[1::2]

# ==== Sampling rate conversion ====
N = int(nframes/20) # Number of input samples
#N = 32767
LW = 32 # width of window (range of x in sinc(x))
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
        if (n+k>=0) and (n+k<N):
            sum = sum + x[int(n+k)] * windowed_sinc(k-dn)
    return sum
    
y = [] # output

#x = np.arange(N)

# ひとまずLchのみSRCしてwav-ファイルとして保存
# RchにもLchと同じ処理をすれば良い
for m1 in range(0, N):
    y.append(convolution(left_data, m1))

int_y=[]

# change format from float to integer
for i in range(0, N):
    int_y.append(int(y[i]))

#plt.plot(x, x1)
#plt.plot(x, y, marker=".", label="1kHz sin-wave @Fs=48kHz") # 1kHz SIN波 @Fs=48kHz

# pack from list to binary-data
outd = struct.pack('h' * len(int_y), *int_y)  # 'h' means "short(16bit)"

# write output data to file in wav-format
waveFile_w.setnchannels(1)
waveFile_w.setsampwidth(samplewidth)
waveFile_w.setframerate(48000)
waveFile_w.writeframesraw(outd)

waveFile_r.close()
waveFile_w.close()
