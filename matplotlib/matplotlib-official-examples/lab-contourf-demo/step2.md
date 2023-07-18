# Create Filled Contour with Automatic Levels

Next, we will create a filled contour plot with automatic levels. We will use the `contourf` method with the `cmap` parameter set to `plt.cm.bone` to specify the colormap. We will also add contour lines with the `contour` method and pass in a subset of the contour levels used for the filled contours.

```python
# Create filled contour with automatic levels
fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, 10, cmap=plt.cm.bone, origin=origin)
CS2 = ax.contour(CS, levels=CS.levels[::2], colors='r', origin=origin)

# Add title, axis labels, and colorbar
ax.set_title('Filled Contour with Automatic Levels')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z Label')
cbar.add_lines(CS2)

# Show plot
plt.show()
```
