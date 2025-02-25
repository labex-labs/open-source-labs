# Tracer les données

Dans cette étape, nous allons tracer les données sur l'objet Axes à l'aide de la fonction `plot` de Matplotlib. Nous allons tracer six lignes différentes avec des pentes différentes et du bruit aléatoire.

```python
ax.plot(x, np.sin(x) + x + noise)
ax.plot(x, np.sin(x) + 0.5 * x + noise)
ax.plot(x, np.sin(x) + 2 * x + noise)
ax.plot(x, np.sin(x) - 0.5 * x + noise)
ax.plot(x, np.sin(x) - 2 * x + noise)
ax.plot(x, np.sin(x) + noise)
```
