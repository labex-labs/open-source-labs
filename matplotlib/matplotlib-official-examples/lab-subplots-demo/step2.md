# Stacking Subplots in One Direction

To create multiple subplots stacked vertically or horizontally, we can pass the number of rows and columns as arguments to the `subplots()` function. The returned `axs` object is a 1D numpy array containing the list of created `Axes`.

```python
fig, axs = plt.subplots(2)
axs[0].plot(x, y)
axs[1].plot(x, -y)
```
