# Génération des données

Nous utiliserons la fonction make_blobs du module sklearn.datasets pour générer un ensemble de données synthétiques avec trois groupes. L'ensemble de données comprendra 750 échantillons avec une écart-type de groupe de 0,4. Nous allons également standardiser les données à l'aide de StandardScaler du module sklearn.preprocessing.

```python
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=750, centers=centers, cluster_std=0.4, random_state=0
)

X = StandardScaler().fit_transform(X)
```
