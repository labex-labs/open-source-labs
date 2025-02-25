# Visualiser les données avec un histogramme 2D - Échelle de couleur linéaire

Dans cette étape, nous allons visualiser les données avec une échelle de couleur linéaire.

```python
# Same data but on linear color scale
pcm = plt.pcolormesh(xedges, yedges, h.T, cmap=cmap,
                         vmax=1.5e2, rasterized=True)
plt.colorbar(pcm, label="# points", pad=0)
plt.title("2D Histogram and Linear Color Scale")
plt.show()
```
