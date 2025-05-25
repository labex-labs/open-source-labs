# Visualizar os Resultados em Dados Reduzidos por PCA

Usaremos PCA para reduzir o conjunto de dados a 2 dimensões e representar graficamente os dados e os clusters neste novo espaço.

```python
import matplotlib.pyplot as plt

reduced_data = PCA(n_components=2).fit_transform(data)
kmeans = KMeans(init="k-means++", n_clusters=n_digits, n_init=4)
kmeans.fit(reduced_data)

# Passo de tamanho da malha. Diminua para aumentar a qualidade do VQ.
h = 0.02  # ponto na malha [x_min, x_max]x[y_min, y_max].

# Representar o limite de decisão. Para isso, atribuiremos uma cor a cada
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obter etiquetas para cada ponto na malha. Utilize o último modelo treinado.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Colocar o resultado num gráfico de cores
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
# Representar os centróides como um X branco
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
    "Agrupamento K-means no conjunto de dados dos dígitos (dados reduzidos por PCA)\n"
    "Os centróides são marcados com uma cruz branca"
)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
```
