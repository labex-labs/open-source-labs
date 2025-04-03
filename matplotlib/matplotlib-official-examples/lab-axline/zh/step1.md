# 绘制垂直线和水平线

我们可以分别使用 `axvline` 和 `axhline` 来绘制垂直线和水平线。让我们在 `y=0`、`y=0.5` 和 `y=1.0` 处绘制三条水平线。

```python
import matplotlib.pyplot as plt
import numpy as np

# 生成数据
t = np.linspace(-10, 10, 100)
sig = 1 / (1 + np.exp(-t))

# 绘制水平线
plt.axhline(y=0, color="black", linestyle="--")
plt.axhline(y=0.5, color="black", linestyle=":")
plt.axhline(y=1.0, color="black", linestyle="--")

# 绘制 Sigmoid 函数
plt.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")
plt.xlim(-10, 10)
plt.xlabel("t")
plt.legend(fontsize=14)
plt.show()
```
