# Visualizar datos con un histograma 2D - escala de color lineal

En este paso, visualizaremos los datos con una escala de color lineal.

```python
# Los mismos datos pero con una escala de color lineal
pcm = plt.pcolormesh(xedges, yedges, h.T, cmap=cmap,
                         vmax=1.5e2, rasterized=True)
plt.colorbar(pcm, label="# puntos", pad=0)
plt.title("Histograma 2D y escala de color lineal")
plt.show()
```
