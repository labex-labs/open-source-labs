# Spektrale Einbettung (Spectral Embedding) durchführen

Als nächstes werden wir die Spektrale Einbettung als Manifold Learning durchführen. Die Spektrale Einbettung ist eine Technik, die eine niedrigdimensionale Darstellung der Daten sucht, die die paarweisen Distanzen zwischen den Punkten erhält.

```python
t0 = time()
se = manifold.SpectralEmbedding(n_components=2, n_neighbors=n_neighbors)
trans_data = se.fit_transform(sphere_data).T
t1 = time()
print("Spectral Embedding: %.2g sec" % (t1 - t0))

ax = fig.add_subplot(259)
plt.scatter(trans_data[0], trans_data[1], c=colors, cmap=plt.cm.rainbow)
plt.title("Spectral Embedding (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")
```
