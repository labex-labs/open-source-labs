# 화살표 방향 정의

이제 화살표의 방향을 정의합니다. 이 예제에서는 NumPy 의 삼각 함수를 사용하여 화살표의 방향을 정의합니다. `sin` 및 `cos` 함수는 `x`, `y`, 및 `z` 방향의 화살표 방향을 나타내는 `u`, `v`, 및 `w` 배열을 생성하는 데 사용됩니다.

```python
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))
```
