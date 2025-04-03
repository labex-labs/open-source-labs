# 绘制任意直线

我们可以使用 `axline` 绘制任意方向的直线。让我们绘制一条斜率为 `0.25` 且经过点 `(0, 0.5)` 的直线。

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

# 绘制任意直线
plt.axline((0, 0.5), slope=0.25, color="black", linestyle=(0, (5, 5)))

# 绘制 Sigmoid 函数
plt.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")
plt.xlim(-10, 10)
plt.xlabel("t")
plt.legend(fontsize=14)
plt.show()
```
