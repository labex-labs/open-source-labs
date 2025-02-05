# 使用二维直方图 - 对数颜色刻度可视化数据

在这一步中，我们将把多个时间序列转换为直方图。这样不仅隐藏的信号会更明显，而且这也是一个快得多的过程。我们将在具有对数颜色刻度的二维直方图中绘制 (x, y) 点。

```python
tic = time.time()

# Linearly interpolate between the points in each time series
num_fine = 800
x_fine = np.linspace(x.min(), x.max(), num_fine)
y_fine = np.concatenate([np.interp(x_fine, x, y_row) for y_row in Y])
x_fine = np.broadcast_to(x_fine, (num_series, num_fine)).ravel()

# Plot (x, y) points in 2d histogram with log colorscale
# It is pretty evident that there is some kind of structure under the noise
# You can tune vmax to make signal more visible
cmap = plt.colormaps["plasma"]
cmap = cmap.with_extremes(bad=cmap(0))
h, xedges, yedges = np.histogram2d(x_fine, y_fine, bins=[400, 100])
pcm = plt.pcolormesh(xedges, yedges, h.T, cmap=cmap,
                         norm="log", vmax=1.5e2, rasterized=True)
plt.colorbar(pcm, label="# points", pad=0)
plt.title("2D Histogram and Log Color Scale")
plt.show()

toc = time.time()
print(f"{toc-tic:.3f} sec. elapsed")
```
