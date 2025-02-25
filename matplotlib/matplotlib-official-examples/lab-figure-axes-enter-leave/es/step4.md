# Conectando los Manejadores de Eventos a la Superficie de la Figura

Ahora conectaremos los manejadores de eventos a la superficie de la figura utilizando el método `mpl_connect`. Esto permitirá que los manejadores de eventos se activen cuando el mouse entre o salga de la figura o de los ejes.

```python
fig.canvas.mpl_connect('figure_enter_event', on_enter_figure)
fig.canvas.mpl_connect('figure_leave_event', on_leave_figure)
fig.canvas.mpl_connect('axes_enter_event', on_enter_axes)
fig.canvas.mpl_connect('axes_leave_event', on_leave_axes)
```
