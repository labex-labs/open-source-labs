# Définir les étiquettes et les graduations de Z

Définissez les étiquettes et les graduations de Z en utilisant la méthode `set`. Nous définirons les étiquettes pour les coordonnées X, Y et Z, et définirons les graduations de Z pour montrer la profondeur de la boîte.

```python
# Définir les étiquettes et les graduations de Z
ax.set(
    xlabel='X [km]',
    ylabel='Y [km]',
    zlabel='Z [m]',
    zticks=[0, -150, -300, -450],
)
```
