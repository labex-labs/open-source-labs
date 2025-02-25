# Créer un tracé à échelle linéaire

Le premier type de transformation d'échelle que nous allons explorer est la linéaire. C'est l'échelle par défaut utilisée dans Matplotlib. Pour créer un tracé à échelle linéaire, nous utilisons la méthode `set_yscale()` et nous passons la chaîne de caractères `'linéaire'`. Nous ajoutons également un titre et une grille au tracé.

```python
# linéaire
plt.plot(x, y)
plt.yscale('linéaire')
plt.title('Échelle linéaire')
plt.grid(True)
```
