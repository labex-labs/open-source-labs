# 创建一个绘图

接下来，我们将使用 Matplotlib 的 `imshow` 函数创建一个绘图。此函数在绘图上显示一幅图像。我们还将创建一个带有两个子图的图形。

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.subplots_adjust(wspace=0.5)

im1 = ax1.imshow([[1, 2], [3, 4]])

im2 = ax2.imshow([[1, 2], [3, 4]])
```
