# 构建网格

现在我们将从批次对象构建地图网格。我们将使用`construct_grids`函数来实现这一点。

```python
def construct_grids(batch):
    """从批次对象构建地图网格

    参数
    ----------
    batch : 批次对象
        :func:`fetch_species_distributions` 返回的对象

    返回
    -------
    (xgrid, ygrid) : 一维数组
        与 batch.coverages 中的值对应的网格
    """
    # 角单元格的 x、y 坐标
    xmin = batch.x_left_lower_corner + batch.grid_size
    xmax = xmin + (batch.Nx * batch.grid_size)
    ymin = batch.y_left_lower_corner + batch.grid_size
    ymax = ymin + (batch.Ny * batch.grid_size)

    # 网格单元格的 x 坐标
    xgrid = np.arange(xmin, xmax, batch.grid_size)
    # 网格单元格的 y 坐标
    ygrid = np.arange(ymin, ymax, batch.grid_size)

    return (xgrid, ygrid)

# 调用函数并将结果存储在 xgrid 和 ygrid 中
xgrid, ygrid = construct_grids(data)
```
