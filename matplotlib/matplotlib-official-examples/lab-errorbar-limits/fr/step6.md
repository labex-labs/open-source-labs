# Ajouter des limites supérieures et inférieures

Pour ajouter à la fois des limites supérieures et inférieures aux barre d'erreur, nous allons utiliser les paramètres `uplims` et `lolims` de la fonction `errorbar`. Nous allons également ajouter un marqueur au tracé pour le différencier des précédents.

```python
# y compris les limites supérieures et inférieures
ax.errorbar(x, y + 1.5, xerr=xerr, yerr=yerr, lolims=True, uplims=True,
            marker='o', markersize=8, linestyle='dotted')
```
