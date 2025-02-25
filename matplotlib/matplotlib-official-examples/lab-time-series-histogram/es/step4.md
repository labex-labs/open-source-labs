# Visualizar datos con un histograma 2D - escala de color logarítmica

En este paso, convertiremos las múltiples series de tiempo en un histograma. No solo será más visible la señal oculta, sino que también es un procedimiento mucho más rápido. Representaremos los puntos (x, y) en un histograma 2D con una escala de color logarítmica.

```python
tic = time.time()

# Interpole linealmente entre los puntos de cada serie de tiempo
num_fine = 800
x_fine = np.linspace(x.min(), x.max(), num_fine)
y_fine = np.concatenate([np.interp(x_fine, x, y_row) for y_row in Y])
x_fine = np.broadcast_to(x_fine, (num_series, num_fine)).ravel()

# Grafique los puntos (x, y) en un histograma 2D con escala de color logarítmica
# Es bastante evidente que hay alguna clase de estructura debajo del ruido
# Puede ajustar vmax para que la señal sea más visible
cmap = plt.colormaps["plasma"]
cmap = cmap.with_extremes(bad=cmap(0))
h, xedges, yedges = np.histogram2d(x_fine, y_fine, bins=[400, 100])
pcm = plt.pcolormesh(xedges, yedges, h.T, cmap=cmap,
                         norm="log", vmax=1.5e2, rasterized=True)
plt.colorbar(pcm, label="# puntos", pad=0)
plt.title("Histograma 2D y escala de color logarítmica")
plt.show()

toc = time.time()
print(f"{toc-tic:.3f} sec. transcurridos")
```
