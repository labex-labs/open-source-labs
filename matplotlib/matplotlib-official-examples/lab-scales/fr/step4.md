# Créer un tracé à échelle logarithmique symétrique

Le troisième type de transformation d'échelle que nous allons explorer est la logarithmique symétrique. Ce type d'échelle est utile lorsqu'il s'agit de traiter des données qui contiennent à la fois des valeurs positives et négatives. Pour créer un tracé à échelle logarithmique symétrique, nous utilisons la méthode `set_yscale()` et nous passons la chaîne de caractères `'symlog'`. Nous définissons également le paramètre `linthresh` sur `0,02` pour spécifier la plage de valeurs autour de zéro qui seront mises à l'échelle linéairement. Nous ajoutons également un titre et une grille au tracé.

```python
# symlogarithmique symétrique
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.02)
plt.title('Échelle logarithmique symétrique')
plt.grid(True)
```
