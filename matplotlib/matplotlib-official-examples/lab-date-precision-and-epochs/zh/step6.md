# 使用新的纪元将 datetime 转换为 Matplotlib 日期

既然纪元已设置为新的默认值，我们就可以使用`mdates.date2num`函数将`datetime`对象转换为 Matplotlib 日期。

```python
date1 = datetime.datetime(2020, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```
