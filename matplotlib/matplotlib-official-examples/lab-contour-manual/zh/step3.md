# 创建绘图

下一步是创建绘图。这可以使用ContourSet函数来完成。

```python
fig, ax = plt.subplots()

# 使用filled=True绘制填充等高线。
cs = ContourSet(ax, [0, 1, 2], [filled01, filled12], filled=True, cmap=cm.bone)
cbar = fig.colorbar(cs)

# 等高线（非填充）。
lines = ContourSet(
    ax, [0, 1, 2], [lines0, lines1, lines2], cmap=cm.cool, linewidths=3)
cbar.add_lines(lines)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 4.5),
       title='用户指定的等高线')
```
