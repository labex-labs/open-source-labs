# Set Up the Plot

We will now set up the plot for our simulation. We will create a figure with an x and y limit equal to the maximum length of the pendulum, set the aspect ratio to be equal, and add a grid.

```python
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(-L, 1.))
ax.set_aspect('equal')
ax.grid()
```
