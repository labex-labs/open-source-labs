# Add zooming functionality

We will add the zooming functionality by connecting the xlim_changed and ylim_changed events to the UpdatingRect and MandelbrotDisplay objects.

```python
ax2.callbacks.connect('xlim_changed', rect)
ax2.callbacks.connect('ylim_changed', rect)

ax2.callbacks.connect('xlim_changed', md.ax_update)
ax2.callbacks.connect('ylim_changed', md.ax_update)
ax2.set_title("Zoom here")
```
