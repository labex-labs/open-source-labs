# Create a plot with a vertical colorbar

We will start by creating a plot with a vertical colorbar. We will generate some random data using `randn` from `numpy` and clip the values to the range of -1 to 1. We will then create an `AxesImage` object using `imshow` and the `coolwarm` colormap. Finally, we will add a title to the plot.

```python
# Make plot with vertical (default) colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.coolwarm)
ax.set_title('Gaussian noise with vertical colorbar')
```
