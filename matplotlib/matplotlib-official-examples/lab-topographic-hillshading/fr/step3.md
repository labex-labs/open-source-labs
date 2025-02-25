# Spécifier la taille des cellules

Si vous avez besoin d'une exagération verticale topographiquement précise, ou si vous ne voulez pas deviner quelle valeur `vert_exag` doit être, vous devrez spécifier la taille des cellules de la grille (c'est-à-dire les paramètres `dx` et `dy`). Sinon, toute valeur `vert_exag` que vous spécifiez sera relative à l'espacement de la grille de vos données d'entrée. Dans cette étape, nous calculons les valeurs de `dx` et `dy` en mètres.

```python
dy = 111200 * dy
dx = 111200 * dx * np.cos(np.radians(dem['ymin']))
```
