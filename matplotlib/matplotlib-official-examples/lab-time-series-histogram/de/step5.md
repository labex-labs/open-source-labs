# Daten mit 2D-Histogramm - Lineare Farbskala visualisieren

In diesem Schritt werden wir die Daten mit einer linearen Farbskala visualisieren.

```python
# Same data but on linear color scale
pcm = plt.pcolormesh(xedges, yedges, h.T, cmap=cmap,
                         vmax=1.5e2, rasterized=True)
plt.colorbar(pcm, label="# points", pad=0)
plt.title("2D Histogram and Linear Color Scale")
plt.show()
```
