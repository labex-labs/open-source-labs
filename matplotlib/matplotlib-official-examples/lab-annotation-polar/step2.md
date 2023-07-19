# Create a Polar Graph

Next, we create a polar graph by defining the figure and specifying that it has a polar projection. We also define the radius and theta values to be used in plotting.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
r = np.arange(0, 1, 0.001)
theta = 2 * 2*np.pi * r
line, = ax.plot(theta, r, color='#ee8d18', lw=3)
```
