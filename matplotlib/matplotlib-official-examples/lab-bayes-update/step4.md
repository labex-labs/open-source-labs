# Create Animation

Now that we have defined the `UpdateDist` class, we can create the animation using Matplotlib's `FuncAnimation` class. We create a figure object and an axis object and pass the axis object to the `UpdateDist` class to create a new instance of the class.

```python
fig, ax = plt.subplots()
ud = UpdateDist(ax, prob=0.7)
anim = FuncAnimation(fig, ud, frames=100, interval=100, blit=True)
plt.show()
```

The `FuncAnimation` class takes several arguments:

- `fig`: the figure object
- `ud`: the `UpdateDist` instance
- `frames`: the number of frames to animate
- `interval`: the time between frames in milliseconds
- `blit`: whether to update only the parts of the plot that have changed
