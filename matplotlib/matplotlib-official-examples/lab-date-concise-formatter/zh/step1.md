# 默认格式化器

我们首先来看默认格式化器及其冗长的输出。我们绘制随时间变化的数据，并观察默认格式化器如何显示日期和时间。

```python
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

# 创建时间数据
base = datetime.datetime(2005, 2, 1)
dates = [base + datetime.timedelta(hours=(2 * i)) for i in range(732)]
N = len(dates)
np.random.seed(19680801)
y = np.cumsum(np.random.randn(N))

# 绘制数据
fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))
lims = [(np.datetime64('2005-02'), np.datetime64('2005-04')),
        (np.datetime64('2005-02-03'), np.datetime64('2005-02-15')),
        (np.datetime64('2005-02-03 11:00'), np.datetime64('2005-02-04 13:20'))]
for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
    # 旋转标签...
    for label in ax.get_xticklabels():
        label.set_rotation(40)
        label.set_horizontalalignment('right')
axs[0].set_title('默认日期格式化器')
plt.show()
```
