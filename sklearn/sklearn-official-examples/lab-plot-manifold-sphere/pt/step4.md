# Executar Aprendizado de Variedade por Isomap

Em seguida, executaremos o aprendizado de variedade por Isomap. Isomap é uma técnica de redução não linear de dimensionalidade que busca uma incorporação em dimensão inferior dos dados que mantém as distâncias geodésicas entre todos os pares de pontos.

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
