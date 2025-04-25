# 创建点的 x 和 y 坐标

```python
n_angles = 30
n_radii = 10
min_radius = 0.2
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
```

解释：

- `n_angles` 是圆中角度的数量。
- `n_radii` 是圆的数量。
- `min_radius` 是圆的最小半径。
- `radii` 是半径数组。
- `angles` 是角度数组。
- `x` 是 x 坐标数组。
- `y` 是 y 坐标数组。
