# Vergrößere das Voxelbild

Wir verwenden jetzt die zuvor definierte `explode`-Funktion, um das Voxelbild aufzuschließen und dabei zwischen jedem Voxel Leerraum zu lassen.

```python
filled = np.ones(n_voxels.shape)
filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)
```
