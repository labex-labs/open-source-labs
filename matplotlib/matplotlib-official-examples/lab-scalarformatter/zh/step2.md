# 为示例图表生成数据

我们将为三个图表生成数据，以展示使用 `~.axes.Axes.ticklabel_format` 时可能的不同配置。

```python
x = np.arange(0, 1,.01)

# 图表 1
plot1_x = x * 1e5 + 1e10
plot1_y = x * 1e-10 + 1e-5

# 图表 2
plot2_x = x * 1e5
plot2_y = x * 1e-4

# 图表 3
plot3_x = -x * 1e5 - 1e10
plot3_y = -x * 1e-5 - 1e-10
```
