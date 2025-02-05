# Demo 1 - Colorbar at each axis

We will create a grid of 3 images with a colorbar at each axis using the following code:

```python
grid = ImageGrid(
    fig, 211, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="top", cbar_mode="each", cbar_size="7%", cbar_pad="1%")
grid[0].set(xticks=[-2, 0], yticks=[-2, 0, 2])

for i, (ax, z) in enumerate(zip(grid, ZS)):
    im = ax.imshow(z, origin="lower", extent=extent)
    cb = ax.cax.colorbar(im)
    # Changing the colorbar ticks
    if i in [1, 2]:
        cb.set_ticks([-1, 0, 1])

for ax, im_title in zip(grid, ["Image 1", "Image 2", "Image 3"]):
    add_inner_title(ax, im_title, loc='lower left')
```

- We create a grid of 3 images using `ImageGrid`.
- We set the `cbar_mode` to "each" to add a colorbar at each axis.
- We set the `share_all` parameter to True to share the x and y axes across all the images.
- We set the `cbar_location` parameter to "top" to position the colorbars at the top.
- We set the `xticks` and `yticks` for the first image.
- We loop through each image and add the image to the axis using `imshow`.
- We add a colorbar to each axis using `ax.cax.colorbar`.
- We set the colorbar ticks for the second and third images.
- We add a title to each image using `add_inner_title`.
