# 创建图形和子图

接下来，我们需要为我们的绘图创建一个图形和子图。我们将使用 `add_subplot` 的 `projection` 参数来创建一个极坐标图。

```python
fig = plt.figure()
ax = fig.add_subplot(projection="polar", facecolor="lightgoldenrodyellow")
```
