# 悬停时设置光标

当用户将鼠标悬停在子图上时，我们需要将光标设置为替代光标。我们通过 `motion_notify_event` 事件和 `set_cursor()` 函数来实现这一点。

```python
def hover(event):
    if fig.canvas.widgetlock.locked():
        # 如果缩放/平移工具已启用，则不执行任何操作。
        return

    fig.canvas.set_cursor(
        event.inaxes.cursor_to_use if event.inaxes else Cursors.POINTER)

fig.canvas.mpl_connect('motion_notify_event', hover)
```
