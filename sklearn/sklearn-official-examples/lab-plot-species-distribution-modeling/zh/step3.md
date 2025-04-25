# 构建地图网格

在这一步中，我们将根据数据对象构建地图网格。我们将创建一个名为 construct_grids 的函数，该函数以数据对象作为输入，并返回 xgrid 和 ygrid。

```python
def construct_grids(batch):
    """从批次对象构建地图网格

    参数
    ----------
    batch : 批次对象
        fetch_species_distributions 返回的对象

    返回
    -------
    (xgrid, ygrid) : 一维数组
        与 batch.coverages 中的值相对应的网格
    """
    # 角点单元格的 x、y 坐标
    xmin = batch.x_left_lower_corner + batch.grid_size
    xmax = xmin + (batch.Nx * batch.grid_size)
    ymin = batch.y_left_lower_corner + batch.grid_size
    ymax = ymin + (batch.Ny * batch.grid_size)

    # 网格单元格的 x 坐标
    xgrid = np.arange(xmin, xmax, batch.grid_size)
    # 网格单元格的 y 坐标
    ygrid = np.arange(ymin, ymax, batch.grid_size)

    return (xgrid, ygrid)

# 构建地图网格
xgrid, ygrid = construct_grids(data)
```
