# Imputation par voisins les plus proches à l'aide de KNNImputer

La classe `KNNImputer` fournit une imputation pour remplir les valeurs manquantes en utilisant l'approche des k plus proches voisins. Elle trouve les plus proches voisins pour chaque échantillon avec des valeurs manquantes et impute les valeurs manquantes des caractéristiques en fonction des valeurs des voisins.

```python
from sklearn.impute import KNNImputer
nan = np.nan
X = [[1, 2, nan], [3, 4, 3], [nan, 6, 5], [8, 8, 7]]
imputer = KNNImputer(n_neighbors=2)
imputed_X = imputer.fit_transform(X)
```
