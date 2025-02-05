# 使用时间增量索引执行操作

你可以使用时间增量索引执行操作。

```python
# 将时间增量索引添加到日期时间索引
tdi = pd.TimedeltaIndex(["1 days", pd.NaT, "2 days"])
dti = pd.date_range("20130101", periods=3)
(dti + tdi).to_list()
```
