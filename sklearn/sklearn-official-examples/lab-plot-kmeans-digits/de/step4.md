# Visualisiere die Ergebnisse auf PCA-reduzierten Daten

Wir werden PCA verwenden, um den Datensatz auf 2 Dimensionen zu reduzieren und die Daten und Cluster in diesem neuen Raum zu plotten.

```python
import matplotlib.pyplot as plt

reduced_data = PCA(n_components=2).fit_transform(data)
kmeans = KMeans(init="k-means++", n_clusters=n_digits, n_init=4)
kmeans.fit(reduced_data)

# Schrittweite des Gitters. Verringern, um die Qualität der VQ zu erhöhen.
h = 0.02  # Punkt im Gitter [x_min, x_max]x[y_min, y_max].

# Plot die Entscheidungsgrenze. Dazu werden wir jeder
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Erhalte Labels für jeden Punkt im Gitter. Verwende das zuletzt trainierte Modell.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Bringe das Ergebnis in einen Farbplot
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
# Plot die Zentren als weißes X
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
