# 간단한 선 그래프 생성

간단한 선 그래프를 생성하는 것으로 시작해 보겠습니다. 이 예제에서는 [0, 2π] 구간에서 사인 (sine) 및 코사인 (cosine) 함수를 플롯 (plot) 합니다.

```python
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin')
plt.plot(x, y2, label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.show()
```
