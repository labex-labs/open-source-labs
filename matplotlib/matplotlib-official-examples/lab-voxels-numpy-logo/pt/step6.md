# Criar o gráfico de voxel

Finalmente, criamos o gráfico de voxel 3D usando a função `voxels` da classe `Axes3D` em Matplotlib.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
ax.set_aspect('equal')

plt.show()
```
