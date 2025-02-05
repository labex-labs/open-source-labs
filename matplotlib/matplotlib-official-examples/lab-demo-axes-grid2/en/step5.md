# Demo 2 - Shared colorbar

We will create a grid of 3 images with a shared colorbar using the following code:

```python
grid2 = ImageGrid(
    fig, 212, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="right", cbar_mode="single", cbar_size="10%", cbar_pad=0.05)
grid2[0].set(xlabel="X", ylabel="Y", xticks=[-2, 0], yticks=[-2, 0, 2])

clim = (np.min(ZS), np.max(ZS))
for ax, z in zip(grid2, ZS):
    im = ax.imshow(z, clim=clim, origin="lower", extent=extent)

# With cbar_mode="single", cax attribute of all axes are identical.
ax.cax.colorbar(im)

for ax, im_title in zip(grid2, ["(a)", "(b)", "(c)"]):
    add_inner_title(ax, im_title, loc='upper left')
```

- We create a grid of 3 images using `ImageGrid`.
- We set the `cbar_mode` to "single" to add a shared colorbar.
- We set the `share_all` parameter to True to share the x and y axes across all the images.
- We set the `cbar_location` parameter to "right" to position the colorbar at the right.
- We set the `xticks` and `yticks` for the first image.
- We loop through each image and add the image to the axis using `imshow`.
- We set the `clim` parameter to ensure that all images use the same color scale.
- We add a shared colorbar to the axis using `ax.cax.colorbar`.
- We add a title to each image using `add_inner_title`.
