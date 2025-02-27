# Marquer les valeurs imputées à l'aide de MissingIndicator

Le transformateur `MissingIndicator` est utile pour indiquer la présence de valeurs manquantes dans un ensemble de données. Il peut être utilisé en conjonction avec l'imputation pour conserver des informations sur les valeurs qui ont été imputées. Ce transformateur renvoie une matrice binaire indiquant la présence de valeurs manquantes dans l'ensemble de données.

```python
from sklearn.impute import MissingIndicator
X = np.array([[-1, -1, 1, 3], [4, -1, 0, -1], [8, -1, 1, 0]])
indicator = MissingIndicator()
mask_missing_values_only = indicator.fit_transform(X)
```
