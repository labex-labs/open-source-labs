# 绘制数据

现在我们将在刚刚创建的坐标轴上绘制数据。我们将使用`plot()`方法以不同的颜色和线宽绘制三个正弦波。

```python
# 绘制数据
ax.plot(X, Y1, c='C0', lw=2.5, label="Blue signal", zorder=10)
ax.plot(X, Y2, c='C1', lw=2.5, label="Orange signal")
ax.plot(X[::3], Y3[::3], linewidth=0, markersize=9,
        marker='s', markerfacecolor='none', markeredgecolor='C4',
        markeredgewidth=2.5)
```
