# Ajouter des limites aux deux axes x et y

Enfin, nous allons ajouter des limites aux deux axes x et y. Nous utiliserons les paramètres `xlolims` et `xuplims` pour ajouter des limites aux barre d'erreur de l'axe x.

```python
# Trace une série avec des limites inférieures et supérieures sur x et y
# erreur constante sur x avec erreur variable sur y
xerr = 0.2
yerr = np.full_like(x, 0.2)
yerr[[3, 6]] = 0.3

# simulez quelques limites en modifiant les données précédentes
xlolims = lolims
xuplims = uplims
lolims = np.zeros_like(x)
uplims = np.zeros_like(x)
lolims[[6]] = True  # seulement limitée à cet indice
uplims[[3]] = True  # seulement limitée à cet indice

# effectuez le tracé
ax.errorbar(x, y + 2.1, xerr=xerr, yerr=yerr,
            xlolims=xlolims, xuplims=xuplims,
            uplims=uplims, lolims=lolims,
            marker='o', markersize=8, linestyle='none')
```
