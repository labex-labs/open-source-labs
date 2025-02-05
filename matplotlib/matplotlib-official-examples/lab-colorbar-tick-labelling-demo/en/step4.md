# Create a plot with a horizontal colorbar

We will now create a plot with a horizontal colorbar. We will follow the same steps as in Step 2, but this time we will use the `afmhot` colormap and set the orientation of the colorbar to horizontal.

```python
# Make plot with horizontal colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.afmhot)
ax.set_title('Gaussian noise with horizontal colorbar')

cbar = fig.colorbar(cax, ticks=[-1, 0, 1], orientation='horizontal')
cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])  # horizontal colorbar
```
