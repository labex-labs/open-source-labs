# Crear el gráfico de voxeles 3D

Ahora creamos el gráfico de voxeles 3D utilizando la función `ax.voxels`. Pasamos `x`, `y`, `z` y `sphere` como parámetros. También agregamos `facecolors` y `edgecolors` utilizando la matriz `colors` que definimos anteriormente.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(x, y, z, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # brighter
          linewidth=0.5)
```
