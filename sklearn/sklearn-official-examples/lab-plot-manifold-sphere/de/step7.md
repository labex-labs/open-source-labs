# t-verteilte stochastische Nachbar-Einbettung (t-distributed Stochastic Neighbor Embedding, t-SNE) durchführen

Schließlich werden wir die t-verteilte stochastische Nachbar-Einbettung (t-SNE) als Manifold Learning durchführen. t-SNE ist eine Technik, die eine niedrigdimensionale Darstellung der Daten sucht, die die lokalen Distanzen zwischen den Punkten erhält.

```python
t0 = time()
tsne = manifold.TSNE(n_components=2, random_state=0)
trans_data = tsne.fit_transform(sphere_data).T
t1 = time()
print("t-SNE: %.2g sec" % (t1 - t0))

ax = fig.add_subplot(2, 5, 10)
plt.scatter(trans_data[0], trans_data[1], c=colors, cmap=plt.cm.rainbow)
plt.title("t-SNE (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")

plt.show()
```
