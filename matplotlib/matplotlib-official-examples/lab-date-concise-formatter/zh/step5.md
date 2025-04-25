# 注册带有本地化的转换器

我们还可以通过向 `~.dates.ConciseDateConverter` 传递关键字参数，并向单位注册表注册你将使用的数据类型，来注册一个带有本地化的转换器。

```python
import datetime

formats = ['%y',          # 刻度大多是年份
           '%b',     # 刻度大多是月份
           '%d',     # 刻度大多是日期
           '%H:%M',  # 小时
           '%H:%M',  # 分钟
           '%S.%f', ]  # 秒
# 这些可以相同，只是偏移一个级别....
zero_formats = [''] + formats[:-1]
#...除了刻度大多是小时的情况，此时有月 - 日格式会更好
zero_formats[3] = '%d-%b'
offset_formats = ['',
                  '%Y',
                  '%b %Y',
                  '%d %b %Y',
                  '%d %b %Y',
                  '%d %b %Y %H:%M', ]

converter = mdates.ConciseDateConverter(
    formats=formats, zero_formats=zero_formats, offset_formats=offset_formats)

munits.registry[np.datetime64] = converter
munits.registry[datetime.date] = converter
munits.registry[datetime.datetime] = converter

fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))
for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('注册了非默认格式的简洁日期格式化器')
plt.show()
```
