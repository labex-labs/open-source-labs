# Ajoutez des flèches et du texte d'annotation d'angle

Nous allons ajouter des flèches et du texte d'annotation d'angle à chaque style de flèche croisée. Tout d'abord, nous obtiendrons les coordonnées du haut pour les patches dessinées à _angleA_ et _angleB_. Ensuite, nous définirons les directions de connexion pour les flèches d'annotation. Enfin, nous ajouterons des flèches et du texte d'annotation au tracé.

```python
    # Obtenez les coordonnées du haut pour les patches dessinées à A et B
    patch_tops = [get_point_of_rotated_vertical(center, 0.5, angle)
                  for center, angle in zip(arrow_centers, anglesAB)]
    # Définissez les directions de connexion pour les flèches d'annotation
    connection_dirs = (1, -1) if angle > 0 else (-1, 1)
    # Ajoutez des flèches et du texte d'annotation
    arrowstyle = "Simple, tail_width=0.5, head_width=4, head_length=8"
    for vline, dir, patch_top, angle in zip(vlines, connection_dirs,
                                            patch_tops, anglesAB):
        kw = dict(connectionstyle=f"arc3,rad={dir * 0.5}",
                  arrowstyle=arrowstyle, color="C0")
        ax.add_patch(FancyArrowPatch(vline, patch_top, **kw))
        ax.text(vline[0] - dir * 0.15, y + 0.7, f'{angle}°', ha="center",
                va="center")
```
