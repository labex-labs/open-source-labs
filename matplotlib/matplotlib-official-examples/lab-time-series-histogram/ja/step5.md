# 2 次元ヒストグラム - 線形カラースケールでデータを可視化する

このステップでは、線形カラースケールを使ってデータを可視化します。

```python
# Same data but on linear color scale
pcm = plt.pcolormesh(xedges, yedges, h.T, cmap=cmap,
                         vmax=1.5e2, rasterized=True)
plt.colorbar(pcm, label="# points", pad=0)
plt.title("2D Histogram and Linear Color Scale")
plt.show()
```
