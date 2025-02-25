# Создание Делонева триангуляции

Мы создадим Делонева триангуляцию для точек. Во - первых, мы создадим координаты x и y для точек с использованием NumPy.

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

Затем мы создадим координаты z для точек.

```python
z = (np.cos(radii) * np.cos(3 * angles)).flatten()
```

Далее мы создадим объект Triangulation с использованием функции `Triangulation()` из `matplotlib.tri`. Поскольку мы не указываем треугольники, Делонева триангуляция будет создана автоматически.

```python
triang = tri.Triangulation(x, y)
```

Наконец, мы уберём нежелательные треугольники с использованием функции `set_mask()`. В этом примере мы задаём маску, чтобы исключить треугольники с средним радиусом меньше `min_radius`.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
