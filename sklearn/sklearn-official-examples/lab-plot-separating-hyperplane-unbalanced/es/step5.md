# Graficar las muestras

Vamos a graficar las muestras utilizando la función `scatter` de `matplotlib.pyplot`.

```python
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolors="k")
```
