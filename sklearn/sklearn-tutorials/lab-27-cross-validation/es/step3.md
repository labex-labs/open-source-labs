# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba

Para evaluar el rendimiento de nuestro modelo, necesitamos dividir el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba. Utilizaremos la función `train_test_split` de la biblioteca scikit-learn para hacer esto.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
