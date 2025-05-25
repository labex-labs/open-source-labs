# Marcação de valores imputados usando MissingIndicator

O transformador `MissingIndicator` é útil para indicar a presença de valores ausentes em um conjunto de dados. Ele pode ser usado em conjunto com a imputação para preservar informações sobre quais valores foram imputados. Este transformador retorna uma matriz binária indicando a presença de valores ausentes no conjunto de dados.

```python
from sklearn.impute import MissingIndicator
X = np.array([[-1, -1, 1, 3], [4, -1, 0, -1], [8, -1, 1, 0]])
indicator = MissingIndicator()
mask_missing_values_only = indicator.fit_transform(X)
```
