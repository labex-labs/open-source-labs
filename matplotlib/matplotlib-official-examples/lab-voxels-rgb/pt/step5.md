# Plotando o Gráfico de Voxel (Voxel Plot)

Finalmente, podemos plotar o gráfico de voxel usando a função `ax.voxels`. Passaremos os valores RGB, a condição para a esfera, as cores das faces, as cores das bordas e a espessura da linha.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(r, g, b, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # brighter
          linewidth=0.5)
ax.set(xlabel='r', ylabel='g', zlabel='b')
ax.set_aspect('equal')
plt.show()
```
