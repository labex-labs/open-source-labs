# 定义坐标轴并显示图像

第四步是使用第三步中创建的 `grid_helper` 实例来定义坐标轴。我们还将使用 `imshow` 函数显示一幅图像。

```python
ax1 = fig.add_subplot(axes_class=Axes, grid_helper=grid_helper)
ax1.imshow(np.arange(25).reshape(5, 5), vmax=50, cmap=plt.cm.gray_r, origin="lower")
```
