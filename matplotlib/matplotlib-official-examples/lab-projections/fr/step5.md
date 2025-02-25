# Régler la projection orthographique

Réglez le premier sous-graphique pour utiliser une projection orthographique avec un champ de vision (`FOV`) de 0 degrés et une longueur focale (`focal_length`) infinie.

```python
axs[0].set_proj_type('ortho')  # FOV = 0 deg
axs[0].set_title("'ortho'\nfocal_length = ∞", fontsize=10)
```
