# Delaunay 삼각 분할 생성

점들의 Delaunay 삼각 분할을 생성합니다. 먼저, NumPy 를 사용하여 점들의 x 및 y 좌표를 생성합니다.

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

그런 다음, 점들의 z 좌표를 생성합니다.

```python
z = (np.cos(radii) * np.cos(3 * angles)).flatten()
```

다음으로, `matplotlib.tri`의 `Triangulation()` 함수를 사용하여 Triangulation 객체를 생성합니다. 삼각형을 지정하지 않으므로 Delaunay 삼각 분할이 자동으로 생성됩니다.

```python
triang = tri.Triangulation(x, y)
```

마지막으로, `set_mask()` 함수를 사용하여 원치 않는 삼각형을 마스크 처리합니다. 이 예제에서는 평균 반경이 `min_radius`보다 작은 삼각형을 제외하도록 마스크를 설정합니다.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
