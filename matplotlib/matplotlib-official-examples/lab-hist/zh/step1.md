# 生成数据并绘制简单直方图

要生成一维直方图，我们只需要一个数字向量。对于二维直方图，我们需要第二个向量。我们将在下面生成这两个向量，并展示每个向量的直方图。

```python
import matplotlib.pyplot as plt
import numpy as np

# 创建一个具有固定种子的随机数生成器，以确保可重复性
rng = np.random.default_rng(19680801)

N_points = 100000
n_bins = 20

# 生成两个正态分布
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# 我们可以使用 *bins* 关键字参数设置箱数。
axs[0].hist(dist1, bins=n_bins)
axs[1].hist(dist2, bins=n_bins)

plt.show()
```
