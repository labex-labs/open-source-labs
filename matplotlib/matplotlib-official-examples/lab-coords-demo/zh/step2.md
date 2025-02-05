# 鼠标移动事件

我们可以使用 `motion_notify_event` 方法连接到鼠标移动事件。在这个示例中，当鼠标在绘图区域上移动时，我们会打印出 x 和 y 数据坐标以及 x 和 y 像素坐标。

```python
def on_move(event):
    if event.inaxes:
        print(f'data coords {event.xdata} {event.ydata},',
              f'pixel coords {event.x} {event.y}')

binding_id = plt.connect('motion_notify_event', on_move)
```
