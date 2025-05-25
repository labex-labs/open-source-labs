# Criar o Gráfico de Voxel 3D

Agora, criamos o gráfico de voxel 3D usando a função `ax.voxels`. Passamos `x`, `y`, `z` e `sphere` como parâmetros. Também adicionamos `facecolors` e `edgecolors` usando o array `colors` que definimos anteriormente.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # brighter
          linewidth=0.5)
```
