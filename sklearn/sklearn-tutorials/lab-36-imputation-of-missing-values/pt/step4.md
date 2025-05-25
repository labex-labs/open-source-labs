# Imputação de vizinhos mais próximos usando KNNImputer

A classe `KNNImputer` fornece imputação para preencher valores ausentes usando a abordagem de k-vizinhos mais próximos. Ela encontra os vizinhos mais próximos para cada amostra com valores ausentes e imputa os valores de recursos ausentes com base nos valores dos vizinhos.

```python
from sklearn.impute import KNNImputer
nan = np.nan
X = [[1, 2, nan], [3, 4, 3], [nan, 6, 5], [8, 8, 7]]
imputer = KNNImputer(n_neighbors=2)
imputed_X = imputer.fit_transform(X)
```
