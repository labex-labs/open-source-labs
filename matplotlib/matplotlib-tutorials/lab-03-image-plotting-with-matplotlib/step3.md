# Applying Pseudocolor Schemes

Pseudocolor schemes can be used to enhance contrast and visualize data more easily. If the image is grayscale, we can apply pseudocolor schemes by specifying different colormaps. We can do this by using the `cmap` parameter in the `imshow` function.

```python
lum_img = img[:, :, 0]
plt.imshow(lum_img, cmap="hot")
```
