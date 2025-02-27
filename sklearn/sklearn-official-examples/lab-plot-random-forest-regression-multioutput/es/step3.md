# Dividir los datos en conjuntos de entrenamiento y prueba

Dividiremos nuestros datos en un conjunto de entrenamiento de 400 y un conjunto de prueba de 200 utilizando la función `train_test_split` de scikit-learn.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=400, test_size=200, random_state=4)
```
