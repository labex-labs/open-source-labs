# Plot a Static Graph

In this step, we plot a static graph using `subplots()` method of `FigureCanvas` object. Then, we create a numpy array using `linspace()` method and plot it using `plot()` method of `subplots()` object.

```python
self._static_ax = static_canvas.figure.subplots()
t = np.linspace(0, 10, 501)
self._static_ax.plot(t, np.tan(t), ".")
```
