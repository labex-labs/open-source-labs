# Dividir el conjunto de datos

A continuación, dividimos el conjunto de datos en conjuntos de entrenamiento y prueba. Utilizaremos el 80% de los datos para el entrenamiento y el 20% para la prueba.

```python
# Dividir los datos en conjuntos de entrenamiento/prueba
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Dividir las etiquetas en conjuntos de entrenamiento/prueba
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```
