# Executar t-distributed Stochastic Neighbor Embedding (t-SNE)

Finalmente, executaremos o aprendizado de variedade por t-distributed Stochastic Neighbor Embedding (t-SNE). O t-SNE é uma técnica que busca uma representação de baixa dimensão dos dados que preserva as distâncias locais entre os pontos.

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
