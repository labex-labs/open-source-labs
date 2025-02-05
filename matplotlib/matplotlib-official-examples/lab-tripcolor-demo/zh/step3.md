# 创建伪彩色图

现在，我们将使用 `tripcolor()` 函数创建一个伪彩色图。我们将使用不同的着色方法创建两个图。

```python
# 平面着色图
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tpc = ax1.tripcolor(triang, z, shading='flat')
fig1.colorbar(tpc)
ax1.set_title('Delaunay 三角剖分的伪彩色图，平面着色')

# 高洛德着色图
fig2, ax2 = plt.subplots()
ax2.set_aspect('equal')
tpc = ax2.tripcolor(triang, z, shading='gouraud')
fig2.colorbar(tpc)
ax2.set_title('Delaunay 三角剖分的伪彩色图，高洛德着色')
```
