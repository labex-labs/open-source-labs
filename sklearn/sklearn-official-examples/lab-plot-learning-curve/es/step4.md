# Analizar las curvas de aprendizaje

```python
# Interpretar las curvas de aprendizaje
```

Podemos analizar la curva de aprendizaje del clasificador Naive Bayes. Su forma se puede encontrar con frecuencia en conjuntos de datos más complejos: la puntuación de entrenamiento es muy alta cuando se utilizan pocos ejemplos para el entrenamiento y disminuye al aumentar el número de muestras, mientras que la puntuación de prueba es muy baja al principio y luego aumenta al agregar muestras. Las puntuaciones de entrenamiento y prueba se vuelven más realistas cuando se utilizan todas las muestras para el entrenamiento.

Vemos otra curva de aprendizaje típica para el clasificador SVM con kernel RBF. La puntuación de entrenamiento permanece alta independientemente del tamaño del conjunto de entrenamiento. Por otro lado, la puntuación de prueba aumenta con el tamaño del conjunto de datos de entrenamiento. De hecho, aumenta hasta un punto en el que alcanza un piso. Observar tal piso es una indicación de que puede que no sea útil adquirir nuevos datos para entrenar el modelo ya que el rendimiento de generalización del modelo no aumentará más.
