# 创建第二组阴影线图案

我们将通过把每个图案重复两次来增加密度，从而创建第二组阴影线图案。我们将使用以下列表：

```python
hatches = ['//', '\\\\', '||', '--', '++', 'xx', 'oo', 'OO', '..', '**']
```

我们将使用与之前相同的循环来创建矩形。

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
