# Создание триангуляции

В этом шаге мы создаем координаты x и y точек с использованием `np.linspace` и `np.repeat`. Затем мы используем функцию `function_z`, определенную на шаге 1, для вычисления значений z. Наконец, мы создаем триангуляцию с использованием `tri.Triangulation`.

```python
n_angles = 20
n_radii = 10
min_radius = 0.15
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
z = function_z(x, y)

triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
