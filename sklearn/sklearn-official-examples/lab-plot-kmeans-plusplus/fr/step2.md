# Calculer les graines à partir de K-Means++

Nous allons utiliser la fonction `kmeans_plusplus` de la bibliothèque scikit-learn pour calculer les graines à partir de K-Means++. Cette fonction renvoie les centres initiaux de cluster utilisés pour le regroupement K-Means. Nous allons calculer 4 clusters à l'aide de K-Means++.

```python
# Calculer les graines à partir de K-Means++
centers_init, indices = kmeans_plusplus(X, n_clusters=4, random_state=0)
```
