# Визуализация данных с помощью 2D гистограммы - логарифмическая шкала цвета

В этом шаге мы преобразуем несколько временных рядов в гистограмму. Не только скрытый сигнал станет более видимым, но это также гораздо быстрейший процесс. Мы построим точки (x, y) в 2D гистограмме с логарифмической шкалой цвета.

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
