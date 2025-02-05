# 为表面图创建颜色

在这一步中，我们将为表面图创建颜色。我们将创建一个与网格形状相同的空字符串数组，并用两种颜色以棋盘图案填充它。

```python
# 为表面图创建颜色
colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]
```
