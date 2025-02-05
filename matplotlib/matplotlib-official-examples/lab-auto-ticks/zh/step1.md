# 无 round_numbers 自动限制模式的散点图

在这一步中，我们将创建一个没有 round_numbers 自动限制模式的散点图，并观察刻度自动定位的行为。

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
