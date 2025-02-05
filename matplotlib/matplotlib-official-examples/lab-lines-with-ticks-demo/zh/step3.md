# 使用带刻度路径效果绘制曲线

现在我们将使用带刻度路径效果绘制一条曲线。

```python
# Plot a curved line with ticked style path
ax.plot(x, y, label="Curve", path_effects=[patheffects.withTickedStroke()])

ax.legend()

plt.show()
```
