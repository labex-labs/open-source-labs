# Visualizar los resultados en datos reducidos por PCA

Utilizaremos PCA para reducir el conjunto de datos a 2 dimensiones y graficar los datos y los clusters en este nuevo espacio.

```python
import matplotlib.pyplot as plt

reduced_data = PCA(n_components=2).fit_transform(data)
kmeans = KMeans(init="k-means++", n_clusters=n_digits, n_init=4)
kmeans.fit(reduced_data)

# Tamaño del paso de la malla. Disminuya para aumentar la calidad de la VQ.
h = 0.02  # punto en la malla [x_min, x_max]x[y_min, y_max].

# Grafique el límite de decisión. Para eso, asignaremos un color a cada
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtenga las etiquetas para cada punto en la malla. Utilice el último modelo entrenado.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Coloque el resultado en una gráfica de color
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(
    Z,
    interpolation="nearest",
    extent=(xx.min(), xx.max(), yy.min(), yy.max()),
    cmap=plt.cm.Paired,
    aspect="auto",
    origin="lower",
)

plt.plot(reduced_data[:, 0], reduced_data[:, 1], "k.", markersize=2)
# Grafique los centroides como una X blanca
centroids = kmeans.cluster_centers_
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="x",
    s=169,
    linewidths=3,
    color="w",
    zorder=10,
)
plt.title(
    "Clustering K-means en el conjunto de datos de dígitos (datos reducidos por PCA)\n"
    "Los centroides están marcados con una cruz blanca"
)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
```
