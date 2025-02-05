# 使用自动级别创建填充等高线

接下来，我们将使用自动级别创建一个填充等高线图。我们将使用`contourf`方法，并将`cmap`参数设置为`plt.cm.bone`以指定颜色映射。我们还将使用`contour`方法添加等高线，并传入用于填充等高线的等高线级别的一个子集。

```python
# 使用自动级别创建填充等高线
fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, 10, cmap=plt.cm.bone, origin=origin)
CS2 = ax.contour(CS, levels=CS.levels[::2], colors='r', origin=origin)

# 添加标题、轴标签和颜色条
ax.set_title('使用自动级别创建填充等高线')
ax.set_xlabel('X 标签')
ax.set_ylabel('Y 标签')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z 标签')
cbar.add_lines(CS2)

# 显示图形
plt.show()
```
