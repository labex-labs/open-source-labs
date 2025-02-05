# Generate Data for Example Plots

We will generate data for three plots to demonstrate the different configurations possible with `~.axes.Axes.ticklabel_format`.

```python
x = np.arange(0, 1, .01)

# Plot 1
plot1_x = x * 1e5 + 1e10
plot1_y = x * 1e-10 + 1e-5

# Plot 2
plot2_x = x * 1e5
plot2_y = x * 1e-4

# Plot 3
plot3_x = -x * 1e5 - 1e10
plot3_y = -x * 1e-5 - 1e-10
```
