# Aumentar en tamaño la imagen de voxeles

Ahora utilizamos la función `explode` definida anteriormente para aumentar en tamaño la imagen de voxeles, dejando espacios entre cada voxel.

```python
filled = np.ones(n_voxels.shape)
filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)
```
