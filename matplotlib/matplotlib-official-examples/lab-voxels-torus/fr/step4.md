# Créer le tracé de voxels 3D

Maintenant, nous créons le tracé de voxels 3D en utilisant la fonction `ax.voxels`. Nous passons `x`, `y`, `z` et `sphere` en tant que paramètres. Nous ajoutons également `facecolors` et `edgecolors` en utilisant le tableau `colors` que nous avons défini précédemment.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # plus clair
          linewidth=0.5)
```
