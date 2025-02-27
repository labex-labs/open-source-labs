# Realizar el aprendizaje de variedades con Isomap

A continuación, realizaremos el aprendizaje de variedades con Isomap. Isomap es una técnica de reducción de dimensionalidad no lineal que busca una proyección de baja dimensionalidad de los datos que mantenga las distancias geodesicas entre todos los pares de puntos.

```python
t0 = time()
trans_data = (
    manifold.Isomap(n_neighbors=n_neighbors, n_components=2)
  .fit_transform(sphere_data).T
)
t1 = time()
print("%s: %.2g sec" % ("ISO", t1 - t0))

ax = fig.add_subplot(257)
plt.scatter(trans_data[0], trans_data[1], c=colors, cmap=plt.cm.rainbow)
plt.title("%s (%.2g sec)" % ("Isomap", t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")
```
