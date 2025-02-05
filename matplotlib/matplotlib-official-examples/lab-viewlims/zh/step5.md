# 添加缩放功能

我们将通过把 `xlim_changed` 和 `ylim_changed` 事件连接到 `UpdatingRect` 和 `MandelbrotDisplay` 对象来添加缩放功能。

```python
ax2.callbacks.connect('xlim_changed', rect)
ax2.callbacks.connect('ylim_changed', rect)

ax2.callbacks.connect('xlim_changed', md.ax_update)
ax2.callbacks.connect('ylim_changed', md.ax_update)
ax2.set_title("Zoom here")
```
