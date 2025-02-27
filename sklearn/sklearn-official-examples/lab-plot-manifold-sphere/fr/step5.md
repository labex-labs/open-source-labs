# Effectuer l'échelle multidimensionnelle (MDS)

Nous allons maintenant effectuer l'apprentissage à variété par échelle multidimensionnelle (MDS). MDS est une technique qui cherche une représentation en dimension réduite des données dans laquelle les distances entre les points respectent les distances dans l'espace original de haute dimension.

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
