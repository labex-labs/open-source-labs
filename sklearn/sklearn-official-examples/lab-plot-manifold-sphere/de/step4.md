# Isomap Manifold Learning durchführen

Als nächstes werden wir das Isomap Manifold Learning durchführen. Isomap ist eine nichtlineare Dimensionsreduktionstechnik, die eine niedrigerdimensionale Einbettung der Daten sucht, die die geodätischen Distanzen zwischen allen Punktpaaren aufrechterhält.

```python
t0 = time()
trans_data = (
    manifold.Isomap(n_neighbors=n_neighbors, n_components=2)
  .fit_transform(sphere_data)
  .T
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
