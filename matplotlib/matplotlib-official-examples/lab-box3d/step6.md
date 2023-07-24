# Set Labels and Zticks

Set labels and zticks using the `set` method. We will set the labels for X, Y, and Z coordinates, and set the zticks to show the depth of the box.

```python
# Set labels and zticks
ax.set(
    xlabel='X [km]',
    ylabel='Y [km]',
    zlabel='Z [m]',
    zticks=[0, -150, -300, -450],
)
```
