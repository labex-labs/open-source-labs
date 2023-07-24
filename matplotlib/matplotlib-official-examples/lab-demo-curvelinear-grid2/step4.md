# Define Axes and Display Image

The fourth step is to define the axes using the `grid_helper` instance created in Step 3. We will also display an image using the `imshow` function.

```python
ax1 = fig.add_subplot(axes_class=Axes, grid_helper=grid_helper)
ax1.imshow(np.arange(25).reshape(5, 5), vmax=50, cmap=plt.cm.gray_r, origin="lower")
```
