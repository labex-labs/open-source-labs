# Запуск бенчмарка

Мы сравним три подхода к инициализации K-Means:

- инициализация с использованием `k-means++`. Этот метод является стохастическим, и мы запустим инициализацию 4 раза;
- случайная инициализация. Этот метод также является стохастическим, и мы запустим инициализацию 4 раза;
- инициализация на основе проекции PCA. Мы будем использовать компоненты PCA для инициализации K-Means. Этот метод детерминирован, и одна инициализация достаточно.

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
