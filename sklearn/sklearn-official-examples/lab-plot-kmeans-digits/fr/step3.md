# Exécuter le critère d'évaluation

Nous allons comparer trois approches pour initialiser K-Means :

- une initialisation utilisant `k-means++`. Cette méthode est stochastique et nous exécuterons l'initialisation 4 fois ;
- une initialisation aléatoire. Cette méthode est également stochastique et nous exécuterons l'initialisation 4 fois ;
- une initialisation basée sur une projection PCA. Nous utiliserons les composantes de la PCA pour initialiser K-Means. Cette méthode est déterministe et une seule initialisation suffit.

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
