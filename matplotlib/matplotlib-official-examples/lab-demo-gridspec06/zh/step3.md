# 创建图形和外部网格

接下来，我们将使用`add_gridspec`函数创建图形和外部网格。我们将创建一个 4x4 的网格，子图之间没有间距。

```python
fig = plt.figure(figsize=(8, 8))
outer_grid = fig.add_gridspec(4, 4, wspace=0, hspace=0)
```
