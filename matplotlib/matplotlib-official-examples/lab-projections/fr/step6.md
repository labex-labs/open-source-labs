# Régler les projections perspective

Réglez le deuxième sous-graphique pour utiliser une projection perspective avec le champ de vision (`FOV`) par défaut de 90 degrés et une longueur focale (`focal_length`) de 1.

```python
axs[1].set_proj_type('persp')  # FOV = 90 deg
axs[1].set_title("'persp'\nfocal_length = 1 (default)", fontsize=10)
```

Réglez le troisième sous-graphique pour utiliser une projection perspective avec un champ de vision (`FOV`) de 157,4 degrés et une longueur focale (`focal_length`) de 0,2.

```python
axs[2].set_proj_type('persp', focal_length=0.2)  # FOV = 157.4 deg
axs[2].set_title("'persp'\nfocal_length = 0.2", fontsize=10)
```
