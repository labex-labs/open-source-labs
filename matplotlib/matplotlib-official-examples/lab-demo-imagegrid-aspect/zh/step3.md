# 创建图像网格

我们将创建两个图像网格来显示我们的图像。第一个图像网格将有两行两列，第二个图像网格也将有两行两列。

```python
grid1 = ImageGrid(fig, 121, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
grid2 = ImageGrid(fig, 122, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
```
