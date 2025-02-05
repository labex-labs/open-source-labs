# 创建一个时间增量索引

你可以生成一个包含时间增量的索引。

```python
# 生成一个时间增量索引
pd.TimedeltaIndex(["1 days", "1 days, 00:00:05", np.timedelta64(2, "D"), datetime.timedelta(days=2, seconds=2)])
```
