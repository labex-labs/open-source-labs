# 定义 on_press 函数

接下来，我们定义一个名为 on_press 的函数，该函数将根据在第一个窗口中鼠标点击的位置来调整第二个窗口的 x 和 y 轴范围。

```python
def on_press(event):
    if event.button!= 1:
        return
    x, y = event.xdata, event.ydata
    axzoom.set_xlim(x - 0.1, x + 0.1)
    axzoom.set_ylim(y - 0.1, y + 0.1)
    figzoom.canvas.draw()
```
