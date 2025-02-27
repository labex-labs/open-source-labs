# Dividir el conjunto de datos

Antes de entrenar el clasificador de Árboles de Decisión, necesitamos dividir el conjunto de datos en conjuntos de entrenamiento y prueba. Usaremos el 70% de los datos para el entrenamiento y el 30% para la prueba.

```python
# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```
