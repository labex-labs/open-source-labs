# Beibehalten der Anzahl der Merkmale konstant

Standardmäßig fallen bei scikit - learn - Imputern Spalten mit ausschließlich fehlenden Werten weg. In einigen Fällen ist es jedoch erforderlich, die leeren Merkmale beizubehalten, um die Form der Daten beizubehalten. Dies können wir erreichen, indem wir den Parameter `keep_empty_features` auf `True` setzen.

```python
imputer = SimpleImputer(keep_empty_features=True)
X = np.array([[np.nan, 1], [np.nan, 2], [np.nan, 3]])
imputed_X = imputer.fit_transform(X)
```
