# Stacking Subplots in Two Directions

To create a grid of subplots, we can pass the number of rows and columns as arguments to the `subplots()` function. The returned `axs` object is a 2D NumPy array.

```python
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].plot(x, y, 'tab:orange')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 1].plot(x, -y, 'tab:red')
```
