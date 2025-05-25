# round_numbers autolimit_mode 없이 산점도 그리기

이 단계에서는 round_numbers autolimit_mode 없이 산점도 (scatter plot) 를 생성하고 틱 자동 배치 (tick auto-placement) 의 동작을 관찰합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fig, ax = plt.subplots()
dots = np.linspace(0.3, 1.2, 10)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()
ax.scatter(x, y, c=x+y)
plt.show()
```
