# Ajouter une échelle

Dessinez une barre horizontale d'une longueur de 0,1 dans les coordonnées des données, avec une étiquette fixe en dessous.

```python
asb = AnchoredSizeBar(ax.transData,
                      0.1,
                      r"1$^{\prime}$",
                      loc='lower center',
                      pad=0.1, borderpad=0.5, sep=5,
                      frameon=False)
ax.add_artist(asb)
```
