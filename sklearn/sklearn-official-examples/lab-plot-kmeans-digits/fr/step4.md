# Visualiser les résultats sur les données réduites par PCA

Nous utiliserons la PCA pour réduire l'ensemble de données à 2 dimensions et tracer les données et les clusters dans cet espace nouveau.

```python
import matplotlib.pyplot as plt

reduced_data = PCA(n_components=2).fit_transform(data)
kmeans = KMeans(init="k-means++", n_clusters=n_digits, n_init=4)
kmeans.fit(reduced_data)

# Taille d'étape de la grille. Diminuer pour augmenter la qualité de la VQ.
h = 0.02  # point dans la grille [x_min, x_max]x[y_min, y_max].

# Tracer la frontière de décision. Pour cela, nous allons attribuer une couleur à chaque
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtenir les étiquettes pour chaque point de la grille. Utiliser le dernier modèle entraîné.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Mettre le résultat dans un graphique en couleur
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
# Tracer les centroïdes comme une croix blanche
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
    "K-means clustering on the digits dataset (PCA-reduced data)\n"
    "Centroids are marked with white cross"
)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
```
