# Imputación de características multivariadas utilizando IterativeImputer

La clase `IterativeImputer` es un enfoque más avanzado para imputar valores faltantes. Modela cada característica con valores faltantes como una función de otras características y utiliza esa estimación para la imputación. Aprende iterativamente las relaciones entre las características e imputa los valores faltantes en base a estas relaciones.

```python
imp = IterativeImputer()
X = [[1, 2], [3, 6], [4, 8], [np.nan, 3], [7, np.nan]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [np.nan, 6]]
imputed_X_test = imp.transform(X_test)
```
