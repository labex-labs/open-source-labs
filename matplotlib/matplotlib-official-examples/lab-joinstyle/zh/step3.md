# 设置连接样式

我们可以使用 `Line2D` 对象的 `set_solid_joinstyle()` 方法来设置线条的 `JoinStyle`。我们将创建一个新的线条对象，并将其连接样式设置为 `JoinStyle.bevel`。

```python
line = ax.lines[0]
line.set_solid_joinstyle(JoinStyle.bevel)
```
