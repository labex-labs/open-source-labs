# 设置主刻度和次刻度定位器及格式化器

为了使刻度之间的标签居中，我们需要为 x 轴设置主刻度和次刻度定位器及格式化器。我们将使用 `dates.MonthLocator()` 函数将主刻度和次刻度定位到月份，并使用 `dates.DateFormatter()` 函数将次刻度标签格式化为月份缩写。

```python
import matplotlib.dates as dates
import matplotlib.ticker as ticker

ax.xaxis.set_major_locator(dates.MonthLocator())
# 16 是一个近似值，因为每个月的天数不同。
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=16))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
```
