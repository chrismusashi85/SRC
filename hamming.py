import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
SPLNUM = 36

# フィギュアを設定
fig = plt.figure()

# グリッド線を表示
plt.style.use("ggplot")

# グラフ描画領域を追加
ax = fig.add_subplot(111)

ax.set_xlabel("x", fontsize = 16)
ax.set_ylabel("y", fontsize = 16)

x = np.arange(0, 2*pi, pi/SPLNUM)

y = 0.54-0.46*np.cos(x)

ax.plot(x, y, label = "y = hamming(x)")
