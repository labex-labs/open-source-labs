# Proyección aleatoria gaussiana

Ahora, apliquemos la proyección aleatoria gaussiana para reducir la dimensionalidad de nuestros datos.

```python
transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
```

En este paso, creamos una instancia de la clase `GaussianRandomProjection` y la ajustamos a nuestros datos `X`. Luego, aplicamos la transformación llamando al método `fit_transform`. El resultado se almacena en la variable `X_new`.
