# Create a BboxImage with Text

We start by creating a BboxImage with Text. We create a `text` object with the `text()` method and add it to the `ax1` object. We then create a `BboxImage` object using the `add_artist()` method. We pass the `get_window_extent` method of the `text` object to the `BboxImage` constructor to get the bounding box for the text. We also pass a 1D array of shape (1, 256) to the `data` parameter of the `BboxImage` constructor to create an image.

```python
fig, (ax1, ax2) = plt.subplots(ncols=2)

txt = ax1.text(0.5, 0.5, "test", size=30, ha="center", color="w")
ax1.add_artist(
    BboxImage(txt.get_window_extent, data=np.arange(256).reshape((1, -1))))
```
