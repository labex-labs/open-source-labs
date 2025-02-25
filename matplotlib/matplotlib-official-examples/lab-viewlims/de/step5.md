# Hinzufügen der Zoomefunktionalität

Wir werden die Zoomefunktionalität hinzufügen, indem wir die `xlim_changed`- und `ylim_changed`-Ereignisse an die UpdatingRect- und MandelbrotDisplay-Objekte anbinden.

```python
ax2.callbacks.connect('xlim_changed', rect)
ax2.callbacks.connect('ylim_changed', rect)

ax2.callbacks.connect('xlim_changed', md.ax_update)
ax2.callbacks.connect('ylim_changed', md.ax_update)
ax2.set_title("Zoom hier")
```
