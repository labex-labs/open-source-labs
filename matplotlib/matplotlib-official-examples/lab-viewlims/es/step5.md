# Agregar la funcionalidad de zoom

Agregaremos la funcionalidad de zoom conectando los eventos xlim_changed e ylim_changed a los objetos UpdatingRect y MandelbrotDisplay.

```python
ax2.callbacks.connect('xlim_changed', rect)
ax2.callbacks.connect('ylim_changed', rect)

ax2.callbacks.connect('xlim_changed', md.ax_update)
ax2.callbacks.connect('ylim_changed', md.ax_update)
ax2.set_title("Zoom aquí")
```
