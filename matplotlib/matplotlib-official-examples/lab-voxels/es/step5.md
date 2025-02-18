# Graficar la matriz de voxeles

Finalmente, podemos utilizar la función `Axes3D.voxels` para graficar la matriz de voxeles con los colores especificados.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.show()
```
