# Realizar escalamiento multidimensional (MDS)

Ahora realizaremos el aprendizaje de variedades con escalamiento multidimensional (MDS). MDS es una técnica que busca una representación de baja dimensionalidad de los datos en la que las distancias entre los puntos respeten las distancias en el espacio de alta dimensionalidad original.

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
