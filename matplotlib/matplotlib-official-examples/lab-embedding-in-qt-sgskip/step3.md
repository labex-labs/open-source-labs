# Plot a Dynamic Graph

In this step, we plot a dynamic graph using `subplots()` method of `FigureCanvas` object. Then, we create a numpy array using `linspace()` method and plot it using `plot()` method of `subplots()` object.

```python
self._dynamic_ax = dynamic_canvas.figure.subplots()
t = np.linspace(0, 10, 101)
self._line, = self._dynamic_ax.plot(t, np.sin(t + time.time()))
```
