# Tracer les échantillons

Nous allons tracer les échantillons à l'aide de la fonction `scatter` de `matplotlib.pyplot`.

```python
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolors="k")
```
