# Utiliser la PCA pour projeter l'ensemble de données

La PCA est utilisée pour projeter l'ensemble de données dans un nouvel espace qui conserve la majeure partie de sa variation initiale.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_test_pca = pca.fit(X_train).transform(X_test)
```
