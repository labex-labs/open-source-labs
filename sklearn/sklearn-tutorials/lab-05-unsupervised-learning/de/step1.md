# Clustering mit K-Means

Die erste Technik, die wir erkunden werden, ist das Clustering mit dem K-Means-Algorithmus. K-Means ist ein populärer Clustering-Algorithmus, der darauf abzielt, die Beobachtungen in gut voneinander getrennte Gruppen, genannt Cluster, aufzuteilen. Lassen Sie uns das Iris-Datensatz als Beispiel nehmen, um das Clustering mit K-Means zu demonstrieren.

```python
from sklearn import cluster, datasets

# Lade den Iris-Datensatz
X_iris, y_iris = datasets.load_iris(return_X_y=True)

# Führe das K-Means-Clustering durch
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris)

# Drucke die Cluster-Labels
print(k_means.labels_)
```
