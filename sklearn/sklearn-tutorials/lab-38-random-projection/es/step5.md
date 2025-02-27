# Transformada inversa

Los transformadores de proyección aleatoria tienen la opción de calcular la inversa de la matriz de proyección. Exploraremos esta característica aplicando la transformada inversa a nuestros datos proyectados.

```python
transformer = random_projection.SparseRandomProjection(compute_inverse_components=True)
X_new = transformer.fit_transform(X)

# Compute the inverse transform
X_new_inversed = transformer.inverse_transform(X_new)
```

En este paso, creamos una instancia de la clase `SparseRandomProjection` con el parámetro `compute_inverse_components` establecido en `True`. Luego, ajustamos el transformador a nuestros datos `X` y aplicamos la transformación. Finalmente, calculamos la transformada inversa llamando al método `inverse_transform` en los datos proyectados `X_new`.
