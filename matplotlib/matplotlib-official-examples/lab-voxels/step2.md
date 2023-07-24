# Prepare coordinates

Next, we will prepare the coordinates for our voxel plot. We will be creating an 8x8x8 grid of points using NumPy's `indices` function.

```python
x, y, z = np.indices((8, 8, 8))
```
