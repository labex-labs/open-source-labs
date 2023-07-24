# Set colors

We will now set the colors for each object in the voxel plot. We will do this by creating an empty array of the same shape as the boolean array we created in Step 3, and then setting the color of each object based on its location.

```python
colors = np.empty(voxelarray.shape, dtype=object)
colors[link] = 'red'
colors[cube1] = 'blue'
colors[cube2] = 'green'
```
