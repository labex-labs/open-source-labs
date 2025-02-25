# Crear polígonos

Creamos polígonos utilizando `Polygon()` y los agregamos a la lista de parches.

```python
for i in range(N):
    polygon = Polygon(np.random.rand(N, 2), closed=True)
    patches.append(polygon)
```
