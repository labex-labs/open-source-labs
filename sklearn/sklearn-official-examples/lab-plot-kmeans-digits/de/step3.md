# Führe den Benchmark aus

Wir werden drei Ansätze zum Initialisieren von K-Means vergleichen:

- eine Initialisierung mit `k-means++`. Diese Methode ist stochastisch und wir werden die Initialisierung 4-mal ausführen;
- eine zufällige Initialisierung. Diese Methode ist ebenfalls stochastisch und wir werden die Initialisierung 4-mal ausführen;
- eine Initialisierung basierend auf einer PCA-Projektion. Wir werden die Komponenten der PCA verwenden, um K-Means zu initialisieren. Diese Methode ist deterministisch und eine einzelne Initialisierung ist ausreichend.

```python
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

print(82 * "_")
print("init\t\ttime\tinertia\thomo\tcompl\tv-meas\tARI\tAMI\tsilhouette")

kmeans = KMeans(init="k-means++", n_clusters=n_digits, n_init=4, random_state=0)
bench_k_means(kmeans=kmeans, name="k-means++", data=data, labels=labels)

kmeans = KMeans(init="random", n_clusters=n_digits, n_init=4, random_state=0)
bench_k_means(kmeans=kmeans, name="random", data=data, labels=labels)

pca = PCA(n_components=n_digits).fit(data)
kmeans = KMeans(init=pca.components_, n_clusters=n_digits, n_init=1)
bench_k_means(kmeans=kmeans, name="PCA-based", data=data, labels=labels)

print(82 * "_")
```
