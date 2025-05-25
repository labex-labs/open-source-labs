# 뷰가 아닌 플롯 너비에 따른 화살표 크기 조정

`quiver()` 함수는 quiver plot 을 생성하는 데 사용될 수 있습니다. 기본적으로 플롯의 화살표는 플롯 자체가 아닌 데이터에 따라 크기가 조정됩니다. 이로 인해 플롯 가장자리에 가까운 화살표를 보기 어려울 수 있습니다.

```python
import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
U = np.cos(X)
V = np.sin(Y)

fig1, ax1 = plt.subplots()
ax1.set_title('Arrows scale with plot width, not view')
Q = ax1.quiver(X, Y, U, V, units='width')
qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
plt.show()
```
