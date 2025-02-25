# Establecer el color de las elipses

Establecemos el color de cada elipse en la `EllipseCollection` en función de la suma de sus coordenadas x e y.

```python
ec.set_array((X + Y).ravel())
```
