# 注册一个转换器

如果所有对包含日期的坐标轴的调用都要使用这个转换器来进行，那么使用单位注册表可能是最方便的。我们向单位注册表注册一个转换器，并使用简洁日期格式化器绘制数据。

```python
import datetime
import matplotlib.units as munits

converter = mdates.ConciseDateConverter()
munits.registry[np.datetime64] = converter
munits.registry[datetime.date] = converter
munits.registry[datetime.datetime] = converter

fig, axs = plt.subplots(3, 1, figsize=(6, 6), layout='constrained')
for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('简洁日期格式化器')
plt.show()
```
