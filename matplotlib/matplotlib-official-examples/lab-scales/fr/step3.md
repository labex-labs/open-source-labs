# Créer un tracé à échelle logarithmique

Le prochain type de transformation d'échelle que nous allons explorer est la logarithmique. Pour créer un tracé à échelle logarithmique, nous utilisons la méthode `set_yscale()` et nous passons la chaîne de caractères `'log'`. Nous ajoutons également un titre et une grille au tracé.

```python
# log
plt.plot(x, y)
plt.yscale('log')
plt.title('Échelle logarithmique')
plt.grid(True)
```
