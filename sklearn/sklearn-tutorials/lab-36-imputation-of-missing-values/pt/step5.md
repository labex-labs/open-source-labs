# Mantendo o número de recursos constante

Por padrão, os imputadores do scikit-learn removem colunas contendo apenas valores ausentes. No entanto, em alguns casos, é necessário manter os recursos vazios para preservar a forma dos dados. Podemos conseguir isso definindo o parâmetro `keep_empty_features` como True.

```python
imputer = SimpleImputer(keep_empty_features=True)
X = np.array([[np.nan, 1], [np.nan, 2], [np.nan, 3]])
imputed_X = imputer.fit_transform(X)
```
