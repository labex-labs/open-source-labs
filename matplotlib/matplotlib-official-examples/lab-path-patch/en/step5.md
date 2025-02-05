# Plot Control Points and Connecting Lines

In this step, we plot the control points and connecting lines of the path using the `plot` method of the axes object.

```python
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')
```
