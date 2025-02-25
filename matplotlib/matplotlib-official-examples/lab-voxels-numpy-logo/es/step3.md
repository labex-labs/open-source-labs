# Construir el logotipo de NumPy

Ahora podemos comenzar a construir el logotipo de NumPy utilizando una matriz de NumPy 3D llamada `n_voxels`. Establecemos ciertos elementos de la matriz en `True` para representar la forma del logotipo. También definimos otras dos matrices de NumPy llamadas `facecolors` y `edgecolors` que se utilizarán para colorear los voxeles.

```python
n_voxels = np.zeros((4, 3, 4), dtype=bool)
n_voxels[0, 0, :] = True
n_voxels[-1, 0, :] = True
n_voxels[1, 0, 2] = True
n_voxels[2, 0, 1] = True

facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
```
