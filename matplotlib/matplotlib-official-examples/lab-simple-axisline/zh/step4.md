# 使x轴线在y = 0处可见

现在我们要让x轴线在y = 0处可见。这通过将xzero轴设置为可见来实现。

```python
ax.axis["xzero"].set_visible(True)
ax.axis["xzero"].label.set_text("Axis Zero")
```
