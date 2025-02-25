# 点のx座標とy座標を作成する

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

解説:

- `n_angles`は円の角度の数です。
- `n_radii`は円の数です。
- `min_radius`は円の最小半径です。
- `radii`は半径の配列です。
- `angles`は角度の配列です。
- `x`はx座標の配列です。
- `y`はy座標の配列です。
