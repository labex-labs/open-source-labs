# Graficando el gráfico de voxeles

Finalmente, podemos graficar el gráfico de voxeles usando la función `ax.voxels`. Pasaremos los valores RGB, la condición para la esfera, los colores de las caras, los colores de los bordes y el ancho de línea.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(r, g, b, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # más brillante
          linewidth=0.5)
ax.set(xlabel='r', ylabel='g', zlabel='b')
ax.set_aspect('equal')
plt.show()
```
