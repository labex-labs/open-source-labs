# Criar o gráfico de superfície

Nesta etapa, criaremos o gráfico de superfície com as cores das faces (face colors) provenientes do array que criamos. Também personalizaremos o eixo z.

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
