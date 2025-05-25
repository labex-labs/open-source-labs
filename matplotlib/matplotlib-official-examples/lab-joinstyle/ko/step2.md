# 그래프 생성

그래프를 생성하려면 먼저 플롯하려는 데이터를 정의해야 합니다. 이 예제에서는 `numpy` 라이브러리를 사용하여 샘플 데이터를 생성합니다.

```python
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x)
```

다음으로, `plt.subplots()`를 사용하여 새로운 figure 와 axis 를 생성합니다. 그래프의 x 및 y 제한을 설정한 다음 `plot()`을 사용하여 데이터를 플롯합니다.

```python
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([-1.2, 1.2])
ax.plot(x, y)
```
