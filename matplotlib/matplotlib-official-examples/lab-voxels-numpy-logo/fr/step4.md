# Agrandir l'image en voxels

Nous utilisons maintenant la fonction `explode` définie précédemment pour agrandir l'image en voxels, laissant des espaces entre chaque voxel.

```python
filled = np.ones(n_voxels.shape)
filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)
```
