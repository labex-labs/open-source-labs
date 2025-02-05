# 创建德劳内三角剖分

我们将创建点的德劳内三角剖分。首先，我们将使用 NumPy 创建点的 x 和 y 坐标。

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

然后，我们将创建点的 z 坐标。

```python
z = (np.cos(radii) * np.cos(3 * angles)).flatten()
```

接下来，我们将使用 `matplotlib.tri` 中的 `Triangulation()` 函数创建三角剖分对象。由于我们没有指定三角形，将自动创建德劳内三角剖分。

```python
triang = tri.Triangulation(x, y)
```

最后，我们将使用 `set_mask()` 函数屏蔽不需要的三角形。在这个例子中，我们设置掩码以排除平均半径小于 `min_radius` 的三角形。

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
