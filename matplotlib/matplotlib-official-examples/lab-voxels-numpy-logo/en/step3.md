# Build the NumPy logo

Now we can begin to build the NumPy logo using a 3D NumPy array called `n_voxels`. We set certain elements in the array to True to represent the logo's shape. We also define two other NumPy arrays called `facecolors` and `edgecolors` that will be used to color the voxels.

```python
n_voxels = np.zeros((4, 3, 4), dtype=bool)
n_voxels[0, 0, :] = True
n_voxels[-1, 0, :] = True
n_voxels[1, 0, 2] = True
n_voxels[2, 0, 1] = True

facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
```
