# Imputação de recursos multivariados usando IterativeImputer

A classe `IterativeImputer` é uma abordagem mais avançada para imputar valores ausentes. Ela modela cada recurso com valores ausentes como uma função de outros recursos e usa essa estimativa para a imputação. Ela aprende iterativamente as relações entre os recursos e imputa os valores ausentes com base nessas relações.

```python
imp = IterativeImputer()
X = [[1, 2], [3, 6], [4, 8], [np.nan, 3], [7, np.nan]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [np.nan, 6]]
imputed_X_test = imp.transform(X_test)
```
