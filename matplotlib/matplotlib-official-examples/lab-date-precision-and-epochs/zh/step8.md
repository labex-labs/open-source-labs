# 将 numpy.datetime64 转换为 Matplotlib 日期

`numpy.datetime64` 对象在比 `.datetime` 对象大得多的时间范围内具有微秒精度。然而，目前，Matplotlib 时间仅转换回具有微秒分辨率且年份仅跨度为 0000 到 9999 的 datetime 对象。

```python
date1 = np.datetime64('2000-01-01T00:10:00.000012')
mdate1 = mdates.date2num(date1)
```
