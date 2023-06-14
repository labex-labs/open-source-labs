# Polar Axes

We can create a grid of polar `Axes` by passing the `projection='polar'` parameter to the `subplots()` function.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
ax1.plot(x, y)
ax2.plot(x, y ** 2)
```
