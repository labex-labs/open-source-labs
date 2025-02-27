# Evaluar el modelo

Ahora evaluaremos el modelo entrenado utilizando el conjunto de validación. La métrica de evaluación utilizada aquí es la puntuación R-cuadrado.

```python
# Evaluar el modelo en el conjunto de validación
score = model.score(X_val, y_val)
print("Puntuación de validación:", score)
```
