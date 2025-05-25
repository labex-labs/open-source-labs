# Plotar o array de voxels

Finalmente, podemos usar a função `Axes3D.voxels` para plotar o array de voxels com as cores especificadas.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.show()
```
