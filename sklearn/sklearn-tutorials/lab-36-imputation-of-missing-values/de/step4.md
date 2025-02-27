# Imputation mit den nächsten Nachbarn mit KNNImputer

Die Klasse `KNNImputer` bietet eine Imputation zur Befüllung von fehlenden Werten unter Verwendung des k - nächsten - Nachbarn - Ansatzes. Sie sucht die nächsten Nachbarn für jede Probe mit fehlenden Werten und imputiert die fehlenden Merkmalswerte auf der Grundlage der Werte der Nachbarn.

```python
from sklearn.impute import KNNImputer
nan = np.nan
X = [[1, 2, nan], [3, 4, 3], [nan, 6, 5], [8, 8, 7]]
imputer = KNNImputer(n_neighbors=2)
imputed_X = imputer.fit_transform(X)
```
