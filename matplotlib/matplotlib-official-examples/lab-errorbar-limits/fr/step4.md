# Ajouter des limites supérieures

Pour ajouter des limites supérieures aux barre d'erreur, nous allons utiliser le paramètre `uplims` de la fonction `errorbar`. Nous allons également ajouter une valeur constante de 0,5 aux valeurs de y pour différencier ce tracé du précédent.

```python
# y compris les limites supérieures
ax.errorbar(x, y + 0.5, xerr=xerr, yerr=yerr, uplims=True, linestyle='dotted')
```
