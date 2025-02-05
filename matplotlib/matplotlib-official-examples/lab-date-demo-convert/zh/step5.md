# 设置 x 轴并格式化日期

为了使图表更具可读性，我们将把 x 轴的范围设置为该范围内的第一个和最后一个日期。我们还将分别把主定位器和次定位器设置为 DayLocator 和 HourLocator。最后，我们将使用 DateFormatter 函数来格式化日期。复制并粘贴以下代码：

```python
ax.set_xlim(dates[0], dates[-1])
ax.xaxis.set_major_locator(DayLocator())
ax.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
```
