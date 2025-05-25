# Agrupamento usando K-means

A primeira técnica que exploraremos é o agrupamento usando o algoritmo K-means. K-means é um algoritmo de agrupamento popular que visa dividir as observações em grupos bem separados, chamados clusters. Vamos usar o conjunto de dados Iris como exemplo para demonstrar o agrupamento com K-means.

```python
from sklearn import cluster, datasets

# Carregar o conjunto de dados Iris
X_iris, y_iris = datasets.load_iris(return_X_y=True)

# Executar o agrupamento K-means
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris)

# Imprimir as etiquetas dos clusters
print(k_means.labels_)
```
