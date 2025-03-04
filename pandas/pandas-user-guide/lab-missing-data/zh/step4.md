# 对缺失数据进行计算

我们将对缺失数据进行一些基本的算术和统计计算。

```python
# Perform calculations with missing data
df["one"].sum()
df.mean(axis=1, numeric_only=True)
df.cumsum()
```
