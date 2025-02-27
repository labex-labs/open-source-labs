# Graficar el conjunto de datos con pesos

Graficamos el conjunto de datos con pesos utilizando la biblioteca matplotlib. El tamaño de los puntos es proporcional a su peso.

```python
xx, yy = np.meshgrid(np.linspace(-4, 5, 500), np.linspace(-4, 5, 500))
fig, ax = plt.subplots()
ax.scatter(
    X[:, 0],
    X[:, 1],
    c=y,
    s=sample_weight,
    alpha=0.9,
    cmap=plt.cm.bone,
    edgecolor="black",
)
```
