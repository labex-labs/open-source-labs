# Markieren von imputierten Werten mit MissingIndicator

Der Transformator `MissingIndicator` ist nützlich, um das Vorhandensein fehlender Werte in einem Datensatz anzuzeigen. Es kann in Verbindung mit der Imputation verwendet werden, um Informationen darüber zu bewahren, welche Werte imputiert wurden. Dieser Transformator gibt eine binäre Matrix zurück, die das Vorhandensein fehlender Werte im Datensatz angibt.

```python
from sklearn.impute import MissingIndicator
X = np.array([[-1, -1, 1, 3], [4, -1, 0, -1], [8, -1, 1, 0]])
indicator = MissingIndicator()
mask_missing_values_only = indicator.fit_transform(X)
```
