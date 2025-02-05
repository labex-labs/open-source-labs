# 创建第三组阴影线图案

我们将通过组合两种图案来创建一种新的图案，从而创建第三组阴影线图案。我们将使用以下列表：

```python
hatches = ['/o', '\\|', '|*', '-\\', '+o', 'x*', 'o-', 'O|', 'O.', '*-']
```

我们将使用与之前相同的循环来创建矩形。

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
