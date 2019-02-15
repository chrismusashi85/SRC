
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt

LW = 16 #  x's domain is from -LW/2 to LW/2
SPLNUM = 36

pi = np.pi

# フィギュアを設定
fig = plt.figure()

# グリッド線を表示
plt.style.use("ggplot")

# グラフ描画領域を追加
ax = fig.add_subplot(111)

ax.set_xlabel("x", fontsize = 16)
ax.set_ylabel("y", fontsize = 16)

x = np.arange(-LW/2*pi, LW/2*pi, pi/SPLNUM)

y = np.sinc(x)

ax.plot(x, y, label = "y = sinc(x)")

