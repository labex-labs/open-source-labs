# Set Color Scale and Create Colorbar

Now, we will set the color scale for our images and create a colorbar to show the range of values. We will find the minimum and maximum values for all images and normalize the color scale accordingly.

```python
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)

fig.colorbar(images[0], ax=axs, orientation='horizontal', fraction=.1)
```
