# 创建绘图

现在我们将使用 Matplotlib 创建绘图，方法是向绘图中添加两个 `PathPatch` 对象。一个将是橙色填充形状，另一个将是白色轮廓。

```python
# 设置绘图界限
xmin, ymin = verts.min(axis=0) - 1
xmax, ymax = verts.max(axis=0) + 1

# 创建绘图
fig = plt.figure(figsize=(5, 5), facecolor="0.75")  # 灰色背景
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1,
                  xlim=(xmin, xmax),  # 居中
                  ylim=(ymax, ymin),  # 居中，上下颠倒
                  xticks=[], yticks=[])  # 无刻度

# 添加白色轮廓
ax.add_patch(patches.PathPatch(path, facecolor='none', edgecolor='w', lw=6))

# 添加橙色形状
ax.add_patch(patches.PathPatch(path, facecolor='orange', edgecolor='k', lw=2))

# 显示绘图
plt.show()
```
