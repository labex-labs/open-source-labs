# 创建一个带有插入图缩放和标记插入区域的图像

在第二个子图中，我们将创建一个带有插入图缩放和标记插入区域的图像。这将展示如何使用 `.mark_inset` 方法来标记感兴趣的区域并将其连接到插入图坐标轴。

```python
# 加载图像的示例数据
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 数组
extent = (-3, 4, -4, 3)
Z2 = np.zeros((150, 150))
ny, nx = Z.shape
Z2[30:30+ny, 30:30+nx] = Z

# 在子图中显示图像
ax2.imshow(Z2, extent=extent, origin="lower")

# 在绘图的左上角创建一个放大插入图
axins2 = zoomed_inset_axes(ax2, zoom=6, loc=1)

# 在插入图中显示图像
axins2.imshow(Z2, extent=extent, origin="lower")

# 设置插入图的 x 和 y 轴范围以显示感兴趣的区域
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9
axins2.set_xlim(x1, x2)
axins2.set_ylim(y1, y2)

# 设置插入图坐标轴上的刻度数量
axins2.yaxis.get_major_locator().set_params(nbins=7)
axins2.xaxis.get_major_locator().set_params(nbins=7)

# 隐藏插入图坐标轴上的刻度标签
axins2.tick_params(labelleft=False, labelbottom=False)

# 标记感兴趣的区域并将其连接到插入图坐标轴
mark_inset(ax2, axins2, loc1=2, loc2=4, fc="none", ec="0.5")
```
