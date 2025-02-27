# Realizar la incrustación estocástica de vecinos con distribución t (t-SNE)

Finalmente, realizaremos el aprendizaje de variedades con la incrustación estocástica de vecinos con distribución t (t-SNE). t-SNE es una técnica que busca una representación de baja dimensionalidad de los datos que preserva las distancias locales entre los puntos.

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
