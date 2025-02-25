# Personnalisez les étiquettes d'échelle sur la barre de couleur verticale

Ensuite, nous allons personnaliser les étiquettes d'échelle sur la barre de couleur verticale. Nous allons créer une barre de couleur en utilisant `colorbar` et spécifier les emplacements des échelles à l'aide du paramètre `ticks`. Nous définirons ensuite les étiquettes d'échelle en utilisant `set_yticklabels` sur l'attribut `ax` de l'objet barre de couleur.

```python
# Add colorbar, make sure to specify tick locations to match desired ticklabels
cbar = fig.colorbar(cax, ticks=[-1, 0, 1])
cbar.ax.set_yticklabels(['< -1', '0', '> 1'])  # vertically oriented colorbar
```
