# 마스크 생성

이 예제에서는 원치 않는 삼각형을 제거하기 위해 마스크를 생성합니다. 먼저 매개변수 공간 `radii`와 `angles`를 생성합니다.

```python
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi/n_angles
```
