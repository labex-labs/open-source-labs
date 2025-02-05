# 使用时间增量索引

你可以将时间增量索引用作pandas对象的索引。

```python
# 将时间增量索引用作pandas序列的索引
s = pd.Series(np.arange(100), index=pd.timedelta_range("1 days", periods=100, freq="h"))
```
