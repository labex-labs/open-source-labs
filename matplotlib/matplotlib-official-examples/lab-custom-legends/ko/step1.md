# 선 그리기

이 단계에서는 Matplotlib 라이브러리를 사용하여 일련의 선을 그립니다. 먼저, NumPy 를 사용하여 몇 가지 임의의 데이터를 생성합니다. 다음으로, `cycler` 함수를 사용하여 색상 순환 (color cycle) 을 설정하여 색상 맵을 지정합니다. 마지막으로, `plot` 함수를 사용하여 데이터를 플롯하고 `legend()`를 호출하여 범례를 생성합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Set random state for reproducibility
np.random.seed(19680801)

# Create random data
N = 10
data = (np.geomspace(1, 10, 100) + np.random.randn(N, 100)).T

# Set color cycle
cmap = plt.cm.coolwarm
plt.rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

# Plot data and generate legend
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend()
```
