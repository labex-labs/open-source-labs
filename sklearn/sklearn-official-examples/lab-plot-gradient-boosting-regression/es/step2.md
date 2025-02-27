# Preprocesamiento de datos

A continuación, dividiremos nuestro conjunto de datos para utilizar el 90% para el entrenamiento y dejar el resto para la prueba. También estableceremos los parámetros del modelo de regresión.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=13)

params = {
    "n_estimators": 500,
    "max_depth": 4,
    "min_samples_split": 5,
    "learning_rate": 0.01,
    "loss": "squared_error",
}
```
