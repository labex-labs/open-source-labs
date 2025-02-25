# Création du tracé de surface

Dans cette étape, nous allons créer le tracé de surface avec les couleurs de face issues du tableau que nous avons créé. Nous allons également personnaliser l'axe z.

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
