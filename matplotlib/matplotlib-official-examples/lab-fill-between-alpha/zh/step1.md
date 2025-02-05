# 使用 `fill_between` 增强折线图

第一个示例展示了如何使用 `fill_between` 增强折线图。我们将使用来自谷歌的金融数据创建两个子图，一个是简单的折线图，另一个是填充的折线图。

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# 加载一些示例金融数据
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)

# 创建两个共享 x 轴和 y 轴的子图
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)

pricemin = r.close.min()

ax1.plot(r.date, r.close, lw=2)
ax2.fill_between(r.date, pricemin, r.close, alpha=0.7)

for ax in ax1, ax2:
    ax.grid(True)
    ax.label_outer()

ax1.set_ylabel('price')
fig.suptitle('Google (GOOG) daily closing price')
fig.autofmt_xdate()
```
