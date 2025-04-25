# 总结

在本实验中，我们学习了如何使用 `mpl_toolkits.axes_grid1` 模块通过 Matplotlib 创建自定义坐标轴网格。我们创建了两个示例：一个具有固定的坐标轴大小和填充，另一个具有可缩放的坐标轴大小和固定的填充。我们使用 `Divider` 类将坐标轴矩形划分为一个由 `horiz * vert` 指定大小的网格，并使用 `Divider` 类的 `add_axes()` 方法和 `new_locator()` 方法向图形中添加坐标轴。
