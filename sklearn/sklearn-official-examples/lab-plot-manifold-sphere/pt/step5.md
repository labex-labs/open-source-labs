# Executar Aprendizado de Variedade por Escalonamento Multidimensional (MDS)

Agora, executaremos o aprendizado de variedade por Escalonamento Multidimensional (MDS). MDS é uma técnica que busca uma representação de baixa dimensão dos dados na qual as distâncias entre os pontos respeitam as distâncias no espaço original de alta dimensão.

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
