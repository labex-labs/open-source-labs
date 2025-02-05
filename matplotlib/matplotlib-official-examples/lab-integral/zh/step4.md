# 创建绘图

使用 `subplots` 创建一个图形和轴对象。使用 `plot` 绘制 x 和 y 值。使用 `set_ylim` 将 y 轴范围设置为从 0 开始。

```python
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)
```
