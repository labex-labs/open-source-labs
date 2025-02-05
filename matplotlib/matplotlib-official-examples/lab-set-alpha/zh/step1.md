# 创建具有明确透明度值的柱状图

在这一步中，我们将使用 Matplotlib 中的 `bar` 方法创建一个柱状图。我们将使用 `alpha` 关键字参数来设置透明度值。图表中的所有柱子都将具有相同的透明度值。

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility.
np.random.seed(19680801)

fig, ax = plt.subplots()

x_values = [n for n in range(20)]
y_values = np.random.randn(20)

facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors

ax.bar(x_values, y_values, color=facecolors, edgecolor=edgecolors, alpha=0.5)
ax.set_title("Explicit 'alpha' keyword value\nshared by all bars and edges")

plt.show()
```
