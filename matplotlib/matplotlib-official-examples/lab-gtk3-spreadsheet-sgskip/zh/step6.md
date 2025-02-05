# 创建 Matplotlib 绘图

在这一步中，我们将创建一个 Matplotlib 绘图来显示我们的数据。我们首先创建一个图形并添加一个子图。

```python
fig = Figure(figsize=(6, 4))
self.canvas = FigureCanvas(fig)
vbox.pack_start(self.canvas, True, True, 0)
ax = fig.add_subplot()
```
