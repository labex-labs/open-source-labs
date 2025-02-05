# 绘制垂直线

我们可以使用 `axvline` 在给定的 `x` 位置绘制一条垂直线。让我们在 `x = 0` 处绘制一条垂直线。

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

# 绘制垂直线
plt.axvline(color="grey")

# 绘制Sigmoid函数
plt.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")
plt.xlim(-10, 10)
plt.xlabel("t")
plt.legend(fontsize=14)
plt.show()
```
