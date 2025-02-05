# 带有额外边距的散点图

在这一步中，我们将在仍然遵循整数自动限制模式的同时，使用 `.Axes.set_xmargin` / `.Axes.set_ymargin` 在数据周围设置额外的边距。

```python
fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
ax.set_xmargin(0.8)
plt.show()
```
