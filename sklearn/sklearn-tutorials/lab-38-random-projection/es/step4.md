# Proyección aleatoria dispersa

A continuación, probemos otro tipo de proyección aleatoria llamada proyección aleatoria dispersa.

```python
transformer = random_projection.SparseRandomProjection()
X_new = transformer.fit_transform(X)
```

Aquí, creamos una instancia de la clase `SparseRandomProjection` y la aplicamos a nuestros datos `X` utilizando el método `fit_transform`. El resultado se almacena en la variable `X_new`.
