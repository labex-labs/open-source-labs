# Regresión Ridge

La regresión Ridge es un método de regresión lineal que agrega un término de penalización a la función objetivo de mínimos cuadrados ordinarios. Este término de penalización ayuda a reducir el sobreajuste al contraer los coeficientes hacia cero. La complejidad del modelo se puede controlar mediante el parámetro de regularización.

Ajustemos un modelo de regresión Ridge.

```python
reg = linear_model.Ridge(alpha=0.5)
reg.fit([[0, 0], [0, 0], [1, 1]], [0, 0.1, 1])

print(reg.coef_)
```

- Creamos una instancia de `Ridge` con el parámetro de regularización `alpha` establecido en 0.5.
- Utilizamos el método `fit` para ajustar el modelo a los datos de entrenamiento.
- Imprimimos los coeficientes del modelo de regresión Ridge.
