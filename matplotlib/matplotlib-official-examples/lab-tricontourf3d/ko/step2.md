# 좌표 생성

다음으로, 점의 x, y, z 좌표를 생성합니다. 극좌표 (polar coordinates) 로 메쉬 (mesh) 를 생성하고 x, y, z 를 계산합니다.

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
