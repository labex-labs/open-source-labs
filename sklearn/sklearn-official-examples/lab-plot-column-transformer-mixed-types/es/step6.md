# Dividir los datos

En este paso, dividiremos nuestros datos en conjuntos de entrenamiento y prueba utilizando `train_test_split`.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
```
