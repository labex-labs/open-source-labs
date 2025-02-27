# Dividir datos

Dividiremos el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba. El conjunto de entrenamiento se utilizará para entrenar el modelo, y el conjunto de prueba se utilizará para evaluar el rendimiento del modelo.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```
