# Lasso

El Lasso es un método de regresión lineal que agrega un término de penalización a la función objetivo de mínimos cuadrados ordinarios. El término de penalización tiene el efecto de establecer algunos coeficientes en exactamente cero, lo que permite realizar la selección de características. El Lasso se puede utilizar para la estimación de modelos esparsos.

Ajustemos un modelo Lasso.

```python
reg = linear_model.Lasso(alpha=0.1)
reg.fit([[0, 0], [1, 1]], [0, 1])

print(reg.coef_)
```

- Creamos una instancia de `Lasso` con el parámetro de regularización `alpha` establecido en 0.1.
- Utilizamos el método `fit` para ajustar el modelo a los datos de entrenamiento.
- Imprimimos los coeficientes del modelo Lasso.
