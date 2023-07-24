# Set Zoom and Angle View

Set zoom and angle view using the `view_init` and `set_box_aspect` methods. We will set the angle view to 40 degrees in the X direction and -30 degrees in the Y direction, and the zoom to 0.9.

```python
# Set zoom and angle view
ax.view_init(40, -30, 0)
ax.set_box_aspect(None, zoom=0.9)
```
