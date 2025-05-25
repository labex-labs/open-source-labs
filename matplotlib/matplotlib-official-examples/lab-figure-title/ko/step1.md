# 감쇠 및 비감쇠 진동 플롯 생성

먼저, 감쇠 진동과 비감쇠 진동에 대한 두 개의 서브플롯이 있는 그림을 생성합니다. `np.linspace()` 함수를 사용하여 시간 값의 배열을 생성한 다음, `np.cos()` 및 `np.exp()` 함수를 사용하여 각 유형의 진동에 대한 해당 진폭 값을 플롯합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 5.0, 501)

fig, (ax1, ax2) = plt.subplots(1, 2, layout='constrained', sharey=True)
ax1.plot(x, np.cos(6*x) * np.exp(-x))
ax1.set_title('damped')
ax1.set_xlabel('time (s)')
ax1.set_ylabel('amplitude')

ax2.plot(x, np.cos(6*x))
ax2.set_xlabel('time (s)')
ax2.set_title('undamped')

fig.suptitle('Different types of oscillations', fontsize=16)

plt.show()
```
