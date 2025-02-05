# 可视化主成分分析（PCA）结果

我们可以通过绘制主成分来可视化PCA的结果。我们创建数据的三维散点图，并根据每个点的密度为其着色。然后，我们将前两个主成分绘制为一个平面。我们对数据的两个不同视图重复此过程。

```python
fig = plt.figure(figsize=(10, 5))

# 第一个视图
ax = fig.add_subplot(121, projection="3d", elev=-40, azim=-80)
ax.set_title("视图1")

# 绘制数据
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# 绘制主成分
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

# 第二个视图
ax = fig.add_subplot(122, projection="3d", elev=30, azim=20)
ax.set_title("视图2")

# 绘制数据
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# 绘制主成分
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

plt.show()
```
