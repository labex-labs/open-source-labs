# Dividir los datos

Dividiremos los datos en conjuntos de entrenamiento y prueba utilizando la función `train_test_split` de scikit-learn.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
