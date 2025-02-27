# Dividir datos

Dividiremos el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba utilizando la función `train_test_split`.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.7)
```
