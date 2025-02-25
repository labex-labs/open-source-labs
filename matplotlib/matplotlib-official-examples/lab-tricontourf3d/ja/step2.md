# 座標の作成

次に、点の x、y、z 座標を作成します。極座標でメッシュを作成し、x、y、z を計算します。

```python
n_angles = 48
n_radii = 8
min_radius = 0.25

radii = np.linspace(min_radius, 0.95, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi/n_angles

x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()
```
