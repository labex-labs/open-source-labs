# Upscale the voxel image

We now use the `explode` function defined earlier to upscale the voxel image, leaving gaps between each voxel.

```python
filled = np.ones(n_voxels.shape)
filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)
```
