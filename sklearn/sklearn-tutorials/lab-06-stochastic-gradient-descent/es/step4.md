# Dividir datos

Dividiremos el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba. El conjunto de entrenamiento se utilizará para entrenar el clasificador SGD, mientras que el conjunto de prueba se utilizará para evaluar su rendimiento.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
