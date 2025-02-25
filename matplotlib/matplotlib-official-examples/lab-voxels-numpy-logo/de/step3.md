# Baue das NumPy-Logo

Jetzt können wir beginnen, das NumPy-Logo mit einem 3D-NumPy-Array namens `n_voxels` zu bauen. Wir setzen bestimmte Elemente im Array auf True, um die Form des Logos darzustellen. Wir definieren auch zwei weitere NumPy-Arrays namens `facecolors` und `edgecolors`, die verwendet werden, um die Voxel zu färben.

```python
n_voxels = np.zeros((4, 3, 4), dtype=bool)
n_voxels[0, 0, :] = True
n_voxels[-1, 0, :] = True
n_voxels[1, 0, 2] = True
n_voxels[2, 0, 1] = True

facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
```
