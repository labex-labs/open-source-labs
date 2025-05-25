# 반지름 및 각도 공간 생성

`linspace` 함수를 사용하여 반지름 및 각도 공간을 생성합니다:

```python
# Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]
```
