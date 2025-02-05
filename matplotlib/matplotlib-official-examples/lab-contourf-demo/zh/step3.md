# 使用显式级别创建填充等高线

现在，我们将使用显式级别创建一个填充等高线图。我们将使用`contourf`方法，并将`levels`参数设置为一个值列表，以指定等高线级别。我们还将颜色映射设置为一个颜色列表，并将`extend`参数设置为`'both'`，以显示超出级别范围的值。

```python
# 使用显式级别创建填充等高线
fig, ax = plt.subplots()
levels = [-1.5, -1, -0.5, 0, 0.5, 1]
CS = ax.contourf(X, Y, Z, levels, colors=('r', 'g', 'b'),
                 origin=origin, extend='both')
CS2 = ax.contour(X, Y, Z, levels, colors=('k',),
                 linewidths=(3,), origin=origin)

# 添加标题、轴标签和颜色条
ax.set_title('使用显式级别创建填充等高线')
ax.set_xlabel('X 标签')
ax.set_ylabel('Y 标签')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z 标签')

# 显示图形
plt.show()
```
