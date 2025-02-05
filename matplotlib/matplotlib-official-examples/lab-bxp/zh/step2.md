# 计算箱线图统计量

`matplotlib.cbook` 模块中的 `boxplot_stats()` 函数用于计算箱线图所需的统计量。我们将数据和标签作为参数传入。

```python
# Compute boxplot stats
stats = cbook.boxplot_stats(data, labels=labels, bootstrap=10000)
```
