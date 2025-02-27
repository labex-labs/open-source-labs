# Graficar los puntos de datos

Graficamos los puntos de datos de entrada utilizando la función scatter de Matplotlib.

```python
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor="k", s=20)
```
