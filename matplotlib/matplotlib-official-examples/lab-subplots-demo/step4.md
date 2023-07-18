# Sharing Axes

By default, each `Axes` is scaled individually. To align the horizontal or vertical axis of subplots, we can use the `sharex` or `sharey` parameters.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(x, y)
ax2.plot(x + 1, -y)
```
