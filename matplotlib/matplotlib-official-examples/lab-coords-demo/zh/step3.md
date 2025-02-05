# 鼠标点击事件

我们可以使用 `button_press_event` 方法连接到鼠标点击事件。在这个示例中，当鼠标左键被点击时，我们会断开鼠标移动事件的回调。

```python
from matplotlib.backend_bases import MouseButton

def on_click(event):
    if event.button is MouseButton.LEFT:
        print('disconnecting callback')
        plt.disconnect(binding_id)

plt.connect('button_press_event', on_click)
```
