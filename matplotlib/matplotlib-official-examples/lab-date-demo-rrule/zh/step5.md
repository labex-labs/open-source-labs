# 设置日期并生成随机数据

你需要设置开始日期、结束日期以及时间间隔（delta），时间间隔表示每个日期之间的差值。你还需要为该示例生成随机数据。

```python
date1 = datetime.date(1952, 1, 1)
date2 = datetime.date(2004, 4, 12)
delta = datetime.timedelta(days=100)

dates = drange(date1, date2, delta)
s = np.random.rand(len(dates))
```
