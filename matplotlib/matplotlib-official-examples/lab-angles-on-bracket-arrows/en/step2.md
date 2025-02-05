# Define a function to get the point of a rotated vertical line

We will define a function that takes the origin coordinates, line length, and angle in degrees as inputs and returns the xy coordinates of the vertical line end rotated by the specified angle.

```python
def get_point_of_rotated_vertical(origin, line_length, degrees):
    """Return xy coordinates of the vertical line end rotated by degrees."""
    rad = np.deg2rad(-degrees)
    return [origin[0] + line_length * np.sin(rad),
            origin[1] + line_length * np.cos(rad)]
```
