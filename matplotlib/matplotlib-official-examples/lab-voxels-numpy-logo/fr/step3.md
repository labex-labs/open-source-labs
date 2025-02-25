# Construire le logo de NumPy

Maintenant, nous pouvons commencer à construire le logo de NumPy en utilisant un tableau NumPy 3D appelé `n_voxels`. Nous définissons certains éléments du tableau sur True pour représenter la forme du logo. Nous définissons également deux autres tableaux NumPy appelés `facecolors` et `edgecolors` qui seront utilisés pour colorer les voxels.

```python
n_voxels = np.zeros((4, 3, 4), dtype=bool)
n_voxels[0, 0, :] = True
n_voxels[-1, 0, :] = True
n_voxels[1, 0, 2] = True
n_voxels[2, 0, 1] = True

facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
```
