# 创建一个掩码

在这个例子中，我们创建一个掩码来移除不需要的三角形。我们首先创建参数空间 `radii` 和 `angles`。

```python
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi/n_angles
```
