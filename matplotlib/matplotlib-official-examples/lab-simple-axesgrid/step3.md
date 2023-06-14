# Iterate over the grid and plot the images

We then iterate over the `grid` object using the `zip` function to iterate over both the axes and the image arrays. We plot each image on its corresponding axis using the `imshow` function.

```python
for ax, im in zip(grid, [im1, im2, im3, im4]):
    ax.imshow(im)
```
