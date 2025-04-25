# 粘性边缘

Matplotlib 中的一些绘图函数会使坐标轴范围具有“粘性”，即不受 `margins()` 方法的影响。例如，`imshow()` 和 `pcolor()` 函数期望用户希望坐标轴范围紧密围绕绘图中显示的像素。如果不希望有这种行为，就需要将 `use_sticky_edges` 设置为 `False`。在本步骤中，我们将学习如何解决 Matplotlib 中的粘性边缘问题。

```python
# 创建一个网格
y, x = np.mgrid[:5, 1:6]

# 定义多边形坐标
poly_coords = [
    (0.25, 2.75), (3.25, 2.75),
    (2.25, 0.75), (0.25, 0.75)
]

# 创建子图
fig, (ax1, ax2) = plt.subplots(ncols=2)

# 对 ax1 使用粘性边缘，对 ax2 关闭粘性边缘
ax2.use_sticky_edges = False

# 在两个子图上绘图
for ax, status in zip((ax1, ax2), ('是', '不是')):
    cells = ax.pcolor(x, y, x+y, cmap='inferno', shading='auto') # 粘性
    ax.add_patch(
        Polygon(poly_coords, color='forestgreen', alpha=0.5)
    ) # 非粘性
    ax.margins(x=0.1, y=0.05)
    ax.set_aspect('equal')
    ax.set_title(f'{status} 粘性')

plt.show()
```
