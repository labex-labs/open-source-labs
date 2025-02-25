# Verbinden der Ereignishandler mit der Figurcanvas

Wir werden jetzt die Ereignishandler mit der Figurcanvas über die `mpl_connect`-Methode verbinden. Dadurch werden die Ereignishandler ausgelöst, wenn die Maus in die Figur oder Achse eintritt oder verlässt.

```python
fig.canvas.mpl_connect('figure_enter_event', on_enter_figure)
fig.canvas.mpl_connect('figure_leave_event', on_leave_figure)
fig.canvas.mpl_connect('axes_enter_event', on_enter_axes)
fig.canvas.mpl_connect('axes_leave_event', on_leave_axes)
```
