# `x`, `y`, `z` 점으로 매핑

`radius`, `angle` 쌍을 `x`, `y`, `z` 점으로 매핑합니다.

```python
x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()
```
