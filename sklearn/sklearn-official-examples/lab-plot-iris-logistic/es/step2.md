# Crear una instancia del clasificador de regresión logística y ajustar los datos

Crearemos una instancia del clasificador de regresión logística y ajustaremos los datos.

```python
# Create an instance of Logistic Regression Classifier and fit the data.
logreg = LogisticRegression(C=1e5)
logreg.fit(X, Y)
```
