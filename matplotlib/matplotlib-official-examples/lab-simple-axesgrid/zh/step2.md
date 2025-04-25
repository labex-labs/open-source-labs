# 创建一个图形和一个图像网格对象

接下来，我们使用`plt.figure`函数创建一个`figure`对象，并传入`figsize`参数来设置图形的大小。然后，我们使用`ImageGrid`函数创建一个`ImageGrid`对象，并传入`figure`、作为子图参数的`111`、作为`nrows_ncols`参数的`(2, 2)`以创建一个 2x2 的轴网格，以及作为`axes_pad`参数的`0.1`来设置轴之间的间距。

```python
fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111, nrows_ncols=(2, 2), axes_pad=0.1)
```
