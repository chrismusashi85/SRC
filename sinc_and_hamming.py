
# coding: utf-8

# In[14]:


import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
SPLNUM = 144
LW = 32

# フィギュアを設定
fig = plt.figure()

# グリッド線を表示
plt.style.use("ggplot")

# グラフ描画領域を追加
ax = fig.add_subplot(111)

ax.set_xlabel("x", fontsize = 16)
ax.set_ylabel("y", fontsize = 16)

x1 = np.arange(0, 2*pi, 2*pi/SPLNUM)
y1 = 0.54-0.46*np.cos(x1)

#ax.plot(x1, y1, label = "y = hamming(x)")

x2 = np.arange(-LW/2*pi, LW/2*pi, LW*pi/SPLNUM)
y2 = np.sinc(x2)

#ax.plot(x2, y2, label = "y = sinc(x)")

x3 = np.arange(0, SPLNUM, 1)
y3 = y1 * y2

ax.plot(x3, y1)
ax.plot(x3, y2)
ax.plot(x3, y3, label = "y = hamming(sinc(x))")

