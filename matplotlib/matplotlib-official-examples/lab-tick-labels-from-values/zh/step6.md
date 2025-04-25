# 设置刻度格式化器和定位器

我们使用`set_major_formatter()`方法将 x 轴刻度格式化器设置为在步骤 5 中创建的格式化函数。我们还将 x 轴刻度定位器设置为`MaxNLocator(integer=True)`，以确保刻度值采用整数值。

```python
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
```
