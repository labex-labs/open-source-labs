# 점의 x 및 y 좌표 생성

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

설명:

- `n_angles`는 원의 각도 수입니다.
- `n_radii`는 원의 수입니다.
- `min_radius`는 원의 최소 반지름입니다.
- `radii`는 반지름의 배열입니다.
- `angles`는 각도의 배열입니다.
- `x`는 x 좌표의 배열입니다.
- `y`는 y 좌표의 배열입니다.
