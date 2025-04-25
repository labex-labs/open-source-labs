# 创建数据框

我们可以通过传入一个 numpy 数组来创建一个`DataFrame`，该数组带有日期时间索引和带标签的列。

```python
# 创建一个 pandas 数据框
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df
```
