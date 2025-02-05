# 在 3D 绘图上绘制 2D 数据

第三步是使用 `ax.plot` 和 `ax.scatter` 在 3D 绘图上绘制 2D 数据。`ax.plot` 函数使用 x 轴和 y 轴绘制一条正弦曲线。`ax.scatter` 函数在 x 轴和 z 轴上绘制散点图数据。

```python
# 使用 x 轴和 y 轴绘制一条正弦曲线。
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')

# 在 x 轴和 z 轴上绘制散点图数据（每种颜色 20 个二维点）。
颜色 = ('r', 'g', 'b', 'k')

# 为了可重复性固定随机状态
np.random.seed(19680801)

x = np.random.sample(20 * len(颜色))
y = np.random.sample(20 * len(颜色))
c_list = []
for c in 颜色:
    c_list.extend([c] * 20)
# 通过使用 zdir='y'，这些点的 y 值被固定为 zs 值 0
# 并且 (x, y) 点被绘制在 x 轴和 z 轴上。
ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x, z)')
```
