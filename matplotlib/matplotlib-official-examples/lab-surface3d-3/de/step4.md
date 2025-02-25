# Den Oberflächenplot erstellen

In diesem Schritt werden wir den Oberflächenplot erstellen, wobei die Gesichtsfarben aus dem Array genommen werden, das wir erstellt haben. Wir werden auch die z-Achse anpassen.

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
