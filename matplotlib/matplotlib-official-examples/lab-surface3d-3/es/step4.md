# Crear la representación gráfica de superficie

En este paso, crearemos la representación gráfica de superficie con los colores de las caras tomados de la matriz que creamos. También personalizaremos el eje z.

```python
# Create the surface plot
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0)

# Customize the z axis
ax.set_zlim(-1, 1)
ax.zaxis.set_major_locator(LinearLocator(6))

# Show the plot
plt.show()
```
