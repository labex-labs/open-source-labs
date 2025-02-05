# 插入缺失数据

在这里，我们将了解如何在数据中插入缺失值。

```python
# Insert missing values
s = pd.Series([1., 2., 3.])
s.loc[0] = None
```
