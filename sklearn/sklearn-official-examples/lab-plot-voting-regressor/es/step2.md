# Cargar el conjunto de datos de diabetes

A continuación, cargaremos el conjunto de datos de diabetes en nuestro programa utilizando la función `load_diabetes()` proporcionada por scikit-learn. Esta función devuelve el conjunto de datos como una tupla de dos matrices: una que contiene los datos de características y la otra que contiene los datos de destino. Asignaremos estas matrices a `X` e `y`, respectivamente.

```python
# Cargar el conjunto de datos de diabetes
X, y = load_diabetes(return_X_y=True)
```
