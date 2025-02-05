# 日期格式的本地化

如果默认格式不符合需求，可以通过操作三个字符串列表之一来实现日期格式的本地化。我们将标签修改为“日 月 年”，而不是 ISO 格式的“年 月 日”。

```python
fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))

for nn, ax in enumerate(axs):
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)
    formatter.formats = ['%y',  # 刻度大多是年份
                         '%b',       # 刻度大多是月份
                         '%d',       # 刻度大多是日期
                         '%H:%M',    # 小时
                         '%H:%M',    # 分钟
                         '%S.%f', ]  # 秒
    # 这些大多只是上一级的格式...
    formatter.zero_formats = [''] + formatter.formats[:-1]
    #...除了刻度大多是小时的情况，此时最好有
    # 月-日：
    formatter.zero_formats[3] = '%d-%b'

    formatter.offset_formats = ['',
                                '%Y',
                                '%b %Y',
                                '%d %b %Y',
                                '%d %b %Y',
                                '%d %b %Y %H:%M', ]
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('简洁日期格式化器')
plt.show()
```
