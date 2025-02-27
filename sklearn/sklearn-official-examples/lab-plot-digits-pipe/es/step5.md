# Imprimir los mejores parámetros y puntuación

Imprimiremos los mejores parámetros y la puntuación obtenidos a partir de GridSearchCV.

```python
print("Best parameter (CV score=%0.3f):" % search.best_score_)
print(search.best_params_)
```
