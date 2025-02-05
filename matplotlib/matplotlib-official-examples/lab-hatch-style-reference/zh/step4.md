# 创建第一组阴影线图案

我们将使用以下列表创建第一组阴影线图案：

```python
hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
```

然后，我们将使用一个循环为每种阴影线图案创建一个矩形，并将其添加到一个子图中。

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
