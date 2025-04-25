# 在周末使用默认间隔绘制数据

我们将首先使用 matplotlib 中的`plot`函数，以周末的默认间隔来绘制数据。我们还将使用白色虚线突出显示每日数据中的间隔。

```python
# 在周末以间隔绘制数据
fig, ax1 = plt.subplots(figsize=(6, 3))
ax1.plot(r.date, r.adj_close, 'o-')

# 突出显示每日数据中的间隔
gaps = np.flatnonzero(np.diff(r.date) > np.timedelta64(1, 'D'))
for gap in r[['date', 'adj_close']][np.stack((gaps, gaps + 1)).T]:
    ax1.plot(gap.date, gap.adj_close, 'w--', lw=2)
ax1.legend(handles=[ml.Line2D([], [], ls='--', label='Gaps in daily data')])

ax1.set_title("Plotting Data with Default Gaps on Weekends")
ax1.xaxis.set_major_locator(DayLocator())
ax1.xaxis.set_major_formatter(DateFormatter('%a'))
```
