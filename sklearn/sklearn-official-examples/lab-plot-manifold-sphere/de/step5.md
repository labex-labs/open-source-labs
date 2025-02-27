# Mehrdimensionale Skalierung (Multi-dimensional Scaling, MDS) durchführen

Wir werden nun die Mehrdimensionale Skalierung (MDS) als Manifold Learning durchführen. MDS ist eine Technik, die eine niedrigdimensionale Darstellung der Daten sucht, in der die Distanzen zwischen den Punkten den Distanzen im ursprünglichen hochdimensionalen Raum entsprechen.

```python
t0 = time()
mds = manifold.MDS(2, max_iter=100, n_init=1, normalized_stress="auto")
trans_data = mds.fit_transform(sphere_data).T
t1 = time()
print("MDS: %.2g sec" % (t1 - t0))

ax = fig.add_subplot(258)
plt.scatter(trans_data[0], trans_data[1], c=colors, cmap=plt.cm.rainbow)
plt.title("MDS (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")
```
