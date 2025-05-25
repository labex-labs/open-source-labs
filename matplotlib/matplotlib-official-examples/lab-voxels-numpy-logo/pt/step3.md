# Construir o logotipo do NumPy

Agora podemos começar a construir o logotipo do NumPy usando um array NumPy 3D chamado `n_voxels`. Definimos certos elementos no array como True para representar a forma do logotipo. Também definimos dois outros arrays NumPy chamados `facecolors` e `edgecolors` que serão usados para colorir os voxels.

```python
n_voxels = np.zeros((4, 3, 4), dtype=bool)
n_voxels[0, 0, :] = True
n_voxels[-1, 0, :] = True
n_voxels[1, 0, 2] = True
n_voxels[2, 0, 1] = True

facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
```
