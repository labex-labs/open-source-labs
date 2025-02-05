# 创建图形和外部网格布局

下一步是创建一个图形和一个外部网格布局。在这个例子中，我们将创建一个 1 行 2 列的网格布局。

```python
fig = plt.figure()
gs0 = gridspec.GridSpec(1, 2, figure=fig)
```
