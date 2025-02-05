# 加载图像数据

我们将使用来自 `cbook` 的一个名为 `bivariate_normal.npy` 的示例图像数据来演示图像网格。我们使用 `cbook` 中的 `get_sample_data` 函数加载图像数据。

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
im1 = Z
im2 = Z[:, :10]
im3 = Z[:, 10:]
vmin, vmax = Z.min(), Z.max()
```
