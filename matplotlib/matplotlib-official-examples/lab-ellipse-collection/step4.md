# Set the color of ellipses

We set the color of each ellipse in the `EllipseCollection` based on the sum of its x and y coordinate.

```python
ec.set_array((X + Y).ravel())
```
