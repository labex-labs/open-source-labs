# Delaunay 삼각 측량 생성

점의 x 및 y 좌표를 제공하여 삼각형을 지정하지 않고 Delaunay 삼각 측량 (Delaunay triangulation) 을 생성합니다.

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
triang = tri.Triangulation(x, y)
```
