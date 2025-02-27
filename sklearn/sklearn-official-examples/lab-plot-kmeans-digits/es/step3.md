# Ejecutar la referencia de evaluación

Compararemos tres enfoques para inicializar K-Means:

- una inicialización utilizando `k-means++`. Este método es estocástico y ejecutaremos la inicialización 4 veces;
- una inicialización aleatoria. Este método también es estocástico y ejecutaremos la inicialización 4 veces;
- una inicialización basada en una proyección PCA. Utilizaremos los componentes de la PCA para inicializar K-Means. Este método es determinista y una sola inicialización es suficiente.

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
