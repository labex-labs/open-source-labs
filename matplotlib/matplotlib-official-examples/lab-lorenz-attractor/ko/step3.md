# 초기 매개변수 설정

시뮬레이션을 위한 초기 매개변수를 설정합니다. 여기에는 시간 간격 `dt`, 단계 수 `num_steps`, 그리고 `x`, `y`, `z`의 초기 값이 포함됩니다.

```python
dt = 0.01
num_steps = 10000

xyzs = np.empty((num_steps + 1, 3))  # Need one more for the initial values
xyzs[0] = (0., 1., 1.05)  # Set initial values
```
