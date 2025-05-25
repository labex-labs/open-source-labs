# Aumentar a escala da imagem de voxel

Agora usamos a função `explode` definida anteriormente para aumentar a escala da imagem de voxel, deixando lacunas entre cada voxel.

```python
filled = np.ones(n_voxels.shape)
filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)
```
