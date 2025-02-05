# 执行运算

你可以对时间增量执行数学运算。

```python
# 减去两个时间增量
s = pd.Series(pd.date_range("2012-1-1", periods=3, freq="D"))
s - s.max()
```
