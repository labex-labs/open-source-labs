# Faire tourner les axes et mettre à jour le tracé

Enfin, nous allons faire tourner les axes et mettre à jour le tracé à l'aide d'une boucle `for` qui parcourt une rotation complète de l'élévation, puis de l'azimut, du tangage et de tout. Nous utiliserons la fonction `ax.view_init()` pour mettre à jour la vue de l'axe et le titre, et les fonctions `plt.title()`, `plt.draw()` et `plt.pause()` pour afficher l'animation.

```python
# Faire tourner les axes et mettre à jour le tracé
for angle in range(0, 360*4 + 1):
    # Normaliser l'angle dans la plage [-180, 180] pour l'affichage
    angle_norm = (angle + 180) % 360 - 180

    # Parcourir une rotation complète de l'élévation, puis de l'azimut, du tangage et de tout
    elev = azim = roll = 0
    if angle <= 360:
        elev = angle_norm
    elif angle <= 360*2:
        azim = angle_norm
    elif angle <= 360*3:
        roll = angle_norm
    else:
        elev = azim = roll = angle_norm

    # Mettre à jour la vue de l'axe et le titre
    ax.view_init(elev, azim, roll)
    plt.title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (elev, azim, roll))

    # Afficher l'animation
    plt.draw()
    plt.pause(.001)
```
