# Effectuer l'apprentissage à variété par Isomap

Ensuite, nous allons effectuer l'apprentissage à variété par Isomap. Isomap est une technique de réduction de la dimensionalité non linéaire qui cherche une projection en dimension réduite des données qui conserve les distances géodésiques entre tous les couples de points.

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
