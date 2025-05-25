# 기본 pcolormesh

일반적으로 우리는 사변형의 가장자리와 사변형의 값을 정의하여 pcolormesh 를 지정합니다. 여기서 *x*와 *y*는 각각 해당 차원에서 Z 보다 하나의 요소가 더 많다는 점에 유의하십시오.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # len = 11
y = np.arange(4.5, 11, 1)  # len = 7

fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z)
```
