# 创建图形和子图

我们将创建一个包含两个子图的图形。第一个子图将是一个三维曲面图，第二个子图将是一个三维线框图。

```python
# 创建一个包含两个子图的图形
fig = plt.figure(figsize=plt.figaspect(0.5))

# 添加第一个具有三维投影的子图
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# 添加第二个具有三维投影的子图
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
```
