# 定义动画函数

动画函数将由 `FuncAnimation()` 函数调用，并用于使用新数据更新图表。在这个例子中，我们将使用一个随时间变化幅度的正弦波来更新折线图的 y 轴值。

```python
def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # 更新数据。
    return line,
```
