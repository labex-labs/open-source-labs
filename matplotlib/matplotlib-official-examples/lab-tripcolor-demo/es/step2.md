# Crear una triangulación de Delaunay

Vamos a crear una triangulación de Delaunay de los puntos. En primer lugar, crearemos las coordenadas x e y de los puntos utilizando NumPy.

```python
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)
angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles
x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
```

Luego, crearemos las coordenadas z de los puntos.

```python
z = (np.cos(radii) * np.cos(3 * angles)).flatten()
```

A continuación, crearemos el objeto Triangulación utilizando la función `Triangulation()` de `matplotlib.tri`. Dado que no estamos especificando los triángulos, se creará automáticamente la triangulación de Delaunay.

```python
triang = tri.Triangulation(x, y)
```

Finalmente, eliminaremos los triángulos no deseados utilizando la función `set_mask()`. En este ejemplo, estamos estableciendo la máscara para excluir los triángulos con un radio promedio menor que `min_radius`.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
