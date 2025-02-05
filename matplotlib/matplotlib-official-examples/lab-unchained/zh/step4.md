# 设置界限并移除刻度

在这一步中，我们将设置 y 轴界限并移除绘图中的刻度。

```python
# Set y limit (or first line is cropped because of thickness)
ax.set_ylim(-1, 70)

# No ticks
ax.set_xticks([])
ax.set_yticks([])
```
