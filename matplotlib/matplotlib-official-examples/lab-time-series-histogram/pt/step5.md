# Visualizar Dados com Histograma 2D - Escala de Cores Linear

Nesta etapa, visualizaremos os dados com uma escala de cores linear.

```python
# Same data but on linear color scale
pcm = plt.pcolormesh(xedges, yedges, h.T, cmap=cmap,
                         vmax=1.5e2, rasterized=True)
plt.colorbar(pcm, label="# points", pad=0)
plt.title("2D Histogram and Linear Color Scale")
plt.show()
```
