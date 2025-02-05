# 创建带有子图的图形

要创建带有子图的图形，你首先需要使用 `plt.figure()` 创建一个图形对象。然后，你可以使用 `fig.subfigures()` 创建子图。

```python
fig = plt.figure()
subfigs = fig.subfigures(2, 1)
```

这将创建一个带有两个子图的图形，一个在另一个之上。
