# Examining Specific Data Ranges

Sometimes, it might be necessary to examine specific data ranges in an image. We can do this by adjusting the colormap limits using the `clim` parameter in the `imshow` function. This allows us to focus on specific regions of the image while sacrificing detail in other regions.

```python
plt.imshow(img, clim=(min_value, max_value))
```
