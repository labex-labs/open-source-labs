# 데이터 포인트 정의

먼저, 플롯에 사용할 데이터 포인트를 정의합니다. 이 예제에서는 `numpy`를 사용하여 사인파에 대한 x 및 y 값 집합을 생성합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# define a list of markevery cases to plot
cases = [
    None,
    8,
    (30, 8),
    [16, 24, 32],
    [0, -1],
    slice(100, 200, 3),
    0.1,
    0.4,
    (0.2, 0.4)
]

# data points
delta = 0.11
x = np.linspace(0, 10 - 2 * delta, 200) + delta
y = np.sin(x) + 1.0 + delta
```
