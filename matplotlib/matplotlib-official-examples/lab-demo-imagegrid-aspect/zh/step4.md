# 设置宽高比

我们将使用 `set_aspect()` 函数把图像网格中单元格的宽高比设置为 2。

```python
for i in [0, 1]:
    grid1[i].set_aspect(2)

for i in [1, 3]:
    grid2[i].set_aspect(2)
```
