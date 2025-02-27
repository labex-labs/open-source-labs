# Entrenar clasificadores

- Crear una cuadrícula logarítmica de los parámetros `gamma` y `C` utilizando `np.logspace`.
- Dividir los datos en conjuntos de entrenamiento y prueba utilizando `StratifiedShuffleSplit`.
- Realizar una búsqueda en cuadrícula utilizando `GridSearchCV` para encontrar los mejores parámetros para el modelo SVM.
- Ajustar un clasificador para todos los parámetros en la versión bidimensional.
