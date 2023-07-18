# Create a figure and add host axes

We create a figure using `plt.figure()` method and add a host axes using `fig.add_axes()` method. Host axes shares the x-scale with parasite axes.

```python
fig = plt.figure()
host = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
```
