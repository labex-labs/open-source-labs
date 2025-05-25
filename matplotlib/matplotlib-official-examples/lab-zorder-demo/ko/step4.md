# 요소의 사용자 정의 순서

또한 요소의 `zorder`를 사용자 정의 순서로 설정할 수 있습니다. 예를 들어, 범례의 `zorder`를 두 선 사이에 설정할 수 있습니다.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 7.5, 100)
plt.rcParams['lines.linewidth'] = 5
plt.figure()
plt.plot(x, np.sin(x), label='zorder=2', zorder=2)  # bottom
plt.plot(x, np.sin(x+0.5), label='zorder=3',  zorder=3)
plt.axhline(0, label='zorder=2.5', color='lightgrey', zorder=2.5)
plt.title('Custom order of elements')
l = plt.legend(loc='upper right')
l.set_zorder(2.5)  # legend between blue and orange line
plt.show()
```
