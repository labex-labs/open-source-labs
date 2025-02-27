# Mantener el número de características constante

Por defecto, los imputadores de scikit-learn eliminan las columnas que contienen solo valores faltantes. Sin embargo, en algunos casos, es necesario mantener las características vacías para mantener la forma de los datos. Esto se puede lograr estableciendo el parámetro `keep_empty_features` en True.

```python
imputer = SimpleImputer(keep_empty_features=True)
X = np.array([[np.nan, 1], [np.nan, 2], [np.nan, 3]])
imputed_X = imputer.fit_transform(X)
```
