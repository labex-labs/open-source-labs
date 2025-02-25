# Добавляем функциональность приближения

Мы добавим функциональность приближения, подключив события xlim_changed и ylim_changed к объектам UpdatingRect и MandelbrotDisplay.

```python
ax2.callbacks.connect('xlim_changed', rect)
ax2.callbacks.connect('ylim_changed', rect)

ax2.callbacks.connect('xlim_changed', md.ax_update)
ax2.callbacks.connect('ylim_changed', md.ax_update)
ax2.set_title("Zoom here")
```
