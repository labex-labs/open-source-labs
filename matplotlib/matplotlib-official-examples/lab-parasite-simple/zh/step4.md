# 添加数据

我们将通过使用 `plot` 函数把数据添加到图表中。我们会将每条线赋给一个变量，以便之后可以引用它。

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par.plot([0, 1, 2], [0, 3, 2], label="Temperature")
```
