# Marcando valores imputados utilizando MissingIndicator

El transformador `MissingIndicator` es útil para indicar la presencia de valores faltantes en un conjunto de datos. Puede utilizarse en combinación con la imputación para preservar información sobre qué valores se imputaron. Este transformador devuelve una matriz binaria que indica la presencia de valores faltantes en el conjunto de datos.

```python
from sklearn.impute import MissingIndicator
X = np.array([[-1, -1, 1, 3], [4, -1, 0, -1], [8, -1, 1, 0]])
indicator = MissingIndicator()
mask_missing_values_only = indicator.fit_transform(X)
```
