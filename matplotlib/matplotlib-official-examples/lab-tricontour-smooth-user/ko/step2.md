# Triangulation (삼각 측량) 생성

이 단계에서는 `np.linspace`와 `np.repeat`를 사용하여 점의 x 및 y 좌표를 생성합니다. 그런 다음, 1 단계에서 정의된 `function_z`를 사용하여 z-값을 계산합니다. 마지막으로, `tri.Triangulation`을 사용하여 Triangulation (삼각 측량) 을 생성합니다.

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
