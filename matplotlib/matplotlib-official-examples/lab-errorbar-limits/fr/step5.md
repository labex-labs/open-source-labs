# Ajouter des limites inférieures

Pour ajouter des limites inférieures aux barre d'erreur, nous allons utiliser le paramètre `lolims` de la fonction `errorbar`. Nous allons également ajouter une valeur constante de 1,0 aux valeurs de y pour différencier ce tracé des précédents.

```python
# y compris les limites inférieures
ax.errorbar(x, y + 1.0, xerr=xerr, yerr=yerr, lolims=True, linestyle='dotted')
```
