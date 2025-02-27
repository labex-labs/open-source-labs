# Regroupement avec K-means

La première technique que nous allons explorer est le regroupement en utilisant l'algorithme K-means. K-means est un algorithme de regroupement populaire qui vise à diviser les observations en groupes bien séparés appelés clusters. Utilisons l'ensemble de données Iris comme exemple pour démontrer le regroupement avec K-means.

```python
from sklearn import cluster, datasets

# Chargez l'ensemble de données Iris
X_iris, y_iris = datasets.load_iris(return_X_y=True)

# Effectuez un regroupement K-means
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris)

# Affichez les étiquettes de cluster
print(k_means.labels_)
```
