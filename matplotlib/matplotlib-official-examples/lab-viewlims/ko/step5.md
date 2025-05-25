# 확대/축소 기능 추가

xlim_changed 및 ylim_changed 이벤트를 UpdatingRect 및 MandelbrotDisplay 객체에 연결하여 확대/축소 기능을 추가합니다.

```python
ax2.callbacks.connect('xlim_changed', rect)
ax2.callbacks.connect('ylim_changed', rect)

ax2.callbacks.connect('xlim_changed', md.ax_update)
ax2.callbacks.connect('ylim_changed', md.ax_update)
ax2.set_title("Zoom here")
```
