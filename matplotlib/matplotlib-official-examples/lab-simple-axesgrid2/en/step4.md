# Display images in the ImageGrid

Finally, we display the images in the ImageGrid using `imshow` function and `zip` function to iterate through the axes in the grid.

```python
for ax, im in zip(grid, [im1, im2, im3]):
    ax.imshow(im, origin="lower", vmin=vmin, vmax=vmax)

plt.show()
```
