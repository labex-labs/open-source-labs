# Tracer l'ensemble de données pondéré

Nous traçons l'ensemble de données pondéré à l'aide de la bibliothèque matplotlib. La taille des points est proportionnelle à son poids.

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
