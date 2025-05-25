# 색상 결합

이제 RGB 색상 구성 요소를 `(17, 17, 17, 3)` 형태의 단일 배열로 결합합니다.

```python
colors = np.zeros(sphere.shape + (3,))
colors[..., 0] = rc
colors[..., 1] = gc
colors[..., 2] = bc
```
