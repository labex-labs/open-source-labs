# Create a plot and set x-axis to logarithmic scale

We create a figure and axes object using `subplots()` method. We then plot the exponential decay function using `semilogx()` method and set the x-axis to a logarithmic scale using `set_xscale()` method. We also add a grid to the plot using `grid()` method.

```python
fig, ax = plt.subplots()

ax.semilogx(t, np.exp(-t / 5.0))
ax.set_xscale('log')
ax.grid()
```
