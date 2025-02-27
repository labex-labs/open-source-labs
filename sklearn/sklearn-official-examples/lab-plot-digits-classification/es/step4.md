# Dividir el conjunto de datos

Dividiremos el conjunto de datos en subconjuntos de entrenamiento y prueba del 50% cada uno, utilizando el método `train_test_split()` de `sklearn.model_selection`.

```python
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)
```
