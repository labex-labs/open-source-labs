# 定义按键事件函数

接下来，我们定义一个函数 `on_press`，当按下某个键时该函数将会被调用。此函数接受一个 `event` 参数，该参数包含了被按下按键的相关信息。在这个示例中，当按下 “x” 键时，我们将切换 x 轴标签的可见性。

```python
def on_press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()
```
