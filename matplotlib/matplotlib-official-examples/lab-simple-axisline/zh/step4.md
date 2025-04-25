# 使 x 轴线在 y = 0 处可见

现在我们要让 x 轴线在 y = 0 处可见。这通过将 xzero 轴设置为可见来实现。

```python
ax.axis["xzero"].set_visible(True)
ax.axis["xzero"].label.set_text("Axis Zero")
```
