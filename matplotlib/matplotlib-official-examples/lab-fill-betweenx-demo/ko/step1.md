# 간단한 fill_betweenx 플롯 그리기

이 단계에서는 `fill_betweenx` 함수를 사용하여 간단한 플롯을 만드는 방법을 배웁니다. 두 곡선 사이의 영역을 채울 것입니다.

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(4 * np.pi * y)

fig, ax = plt.subplots(figsize=(6, 6))

ax.fill_betweenx(y, x1, x2, color='green', alpha=0.5)
ax.plot(x1, y, color='blue')
ax.plot(x2, y, color='red')

plt.show()
```
