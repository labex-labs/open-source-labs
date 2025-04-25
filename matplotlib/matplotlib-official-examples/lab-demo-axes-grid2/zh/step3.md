# 准备示例数据

我们将使用 cbook 中的 `get_sample_data` 函数来获取示例数据。然后，我们将准备要在网格中显示的图像。

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
extent = (-3, 4, -4, 3)
ZS = [Z[i::3, :] for i in range(3)]
extent = extent[0], extent[1]/3., extent[2], extent[3]
```
