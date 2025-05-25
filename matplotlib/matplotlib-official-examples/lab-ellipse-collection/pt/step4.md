# Definir a cor das elipses

Definimos a cor de cada elipse no `EllipseCollection` com base na soma de suas coordenadas x e y.

```python
ec.set_array((X + Y).ravel())
```
