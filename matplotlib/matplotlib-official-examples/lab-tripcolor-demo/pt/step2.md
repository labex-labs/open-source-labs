# Criando uma Triangulação de Delaunay

Criaremos uma triangulação de Delaunay dos pontos. Primeiro, criaremos as coordenadas x e y dos pontos usando NumPy.

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

Em seguida, criaremos as coordenadas z dos pontos.

```python
z = (np.cos(radii) * np.cos(3 * angles)).flatten()
```

Em seguida, criaremos o objeto `Triangulation` usando a função `Triangulation()` de `matplotlib.tri`. Como não estamos especificando os triângulos, a triangulação de Delaunay será criada automaticamente.

```python
triang = tri.Triangulation(x, y)
```

Finalmente, mascararemos os triângulos indesejados usando a função `set_mask()`. Neste exemplo, estamos definindo a máscara para excluir triângulos com um raio médio menor que `min_radius`.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
