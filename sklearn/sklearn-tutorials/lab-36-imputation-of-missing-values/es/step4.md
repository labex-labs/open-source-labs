# Imputación de vecinos más cercanos utilizando KNNImputer

La clase `KNNImputer` proporciona la imputación para llenar valores faltantes utilizando el enfoque de k-Vecinos más Cercanos. Encuentra los vecinos más cercanos para cada muestra con valores faltantes e imputa los valores faltantes de las características en base a los valores de los vecinos.

```python
from sklearn.impute import KNNImputer
nan = np.nan
X = [[1, 2, nan], [3, 4, 3], [nan, 6, 5], [8, 8, 7]]
imputer = KNNImputer(n_neighbors=2)
imputed_X = imputer.fit_transform(X)
```
