# Créer un tracé à échelle logit

Le quatrième type de transformation d'échelle que nous allons explorer est la logit. Ce type d'échelle est utile lorsqu'il s'agit de traiter des données bornées entre 0 et 1. Pour créer un tracé à échelle logit, nous utilisons la méthode `set_yscale()` et nous passons la chaîne de caractères `'logit'`. Nous ajoutons également un titre et une grille au tracé.

```python
# logit
plt.plot(x, y)
plt.yscale('logit')
plt.title('Échelle logit')
plt.grid(True)
```
