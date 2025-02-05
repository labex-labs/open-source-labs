# Connect the draw event to the callback function

We need to connect the `draw_event` to our `on_draw` function.

```python
fig.canvas.mpl_connect('draw_event', on_draw)
```
