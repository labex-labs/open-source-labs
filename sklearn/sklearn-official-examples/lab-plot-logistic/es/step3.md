# Ajustar el clasificador

Después de generar el conjunto de datos, ajustaremos el clasificador utilizando `LogisticRegression` de scikit-learn.

```python
# Fit the classifier
clf = LogisticRegression(C=1e5)
clf.fit(X, y)
```
