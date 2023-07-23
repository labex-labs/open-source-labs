# Connecting the Event Handlers to the Figure Canvas

We will now connect the event handlers to the figure canvas using the `mpl_connect` method. This will allow the event handlers to be triggered when the mouse enters or leaves the figure or axes.

```python
fig.canvas.mpl_connect('figure_enter_event', on_enter_figure)
fig.canvas.mpl_connect('figure_leave_event', on_leave_figure)
fig.canvas.mpl_connect('axes_enter_event', on_enter_axes)
fig.canvas.mpl_connect('axes_leave_event', on_leave_axes)
```
