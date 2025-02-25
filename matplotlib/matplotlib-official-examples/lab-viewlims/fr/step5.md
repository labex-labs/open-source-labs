# Ajoutez la fonctionnalité de zoom

Nous allons ajouter la fonctionnalité de zoom en connectant les événements xlim_changed et ylim_changed aux objets UpdatingRect et MandelbrotDisplay.

```python
ax2.callbacks.connect('xlim_changed', rect)
ax2.callbacks.connect('ylim_changed', rect)

ax2.callbacks.connect('xlim_changed', md.ax_update)
ax2.callbacks.connect('ylim_changed', md.ax_update)
ax2.set_title("Zoom here")
```
