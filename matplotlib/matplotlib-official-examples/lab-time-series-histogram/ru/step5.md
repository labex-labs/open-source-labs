# Визуализация данных с помощью 2D гистограммы - линейная шкала цвета

В этом шаге мы визуализируем данные с линейной шкалой цвета.

```python
# Same data but on linear color scale
pcm = plt.pcolormesh(xedges, yedges, h.T, cmap=cmap,
                         vmax=1.5e2, rasterized=True)
plt.colorbar(pcm, label="# points", pad=0)
plt.title("2D Histogram and Linear Color Scale")
plt.show()
```
