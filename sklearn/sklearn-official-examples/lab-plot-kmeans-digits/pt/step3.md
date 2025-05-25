# Executar o Benchmark

Vamos comparar três abordagens para inicializar o K-Means:

- uma inicialização usando `k-means++`. Este método é estocástico e executaremos a inicialização 4 vezes;
- uma inicialização aleatória. Este método também é estocástico e executaremos a inicialização 4 vezes;
- uma inicialização baseada numa projeção PCA. Usaremos os componentes da PCA para inicializar o K-Means. Este método é determinístico e uma única inicialização é suficiente.

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
