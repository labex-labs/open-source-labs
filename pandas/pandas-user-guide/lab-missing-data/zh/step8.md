# 理解用于表示缺失值的 NA 标量

最后，我们将讨论 pandas 中用于表示缺失值的实验性 `NA` 标量。

```python
s = pd.Series([1, 2, None], dtype="Int64")
s
```
