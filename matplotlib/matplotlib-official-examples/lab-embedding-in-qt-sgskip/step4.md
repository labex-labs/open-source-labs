# Update the Dynamic Graph

In this step, we update the dynamic graph using a timer. We create a new timer object with a callback function `_update_canvas()`. The callback function updates the data of the graph using `set_data()` method of `Line2D` object and redraws the graph using `draw()` method of `FigureCanvas` object.

```python
self._timer = dynamic_canvas.new_timer(50)
self._timer.add_callback(self._update_canvas)
self._timer.start()

def _update_canvas(self):
    t = np.linspace(0, 10, 101)
    self._line.set_data(t, np.sin(t + time.time()))
    self._line.figure.canvas.draw()
```
