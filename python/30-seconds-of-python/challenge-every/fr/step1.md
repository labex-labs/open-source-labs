# Vérifiez si chaque élément de la liste est considéré comme vrai (truthy)

## Problème

Écrivez une fonction appelée `every(lst, fn = lambda x: x)` qui prend une liste `lst` et une fonction `fn` en arguments. La fonction devrait renvoyer `True` si `fn` renvoie `True` pour chaque élément de la liste, et `False` sinon. Si aucune fonction n'est fournie, la fonction devrait utiliser la fonction identité (`lambda x: x`) par défaut.

Pour résoudre ce problème, vous devrez utiliser la fonction `all()` en combinaison avec `map()` et la fonction `fn` fournie pour vérifier si `fn` renvoie `True` pour tous les éléments de la liste.

## Exemple

```python
every([4, 2, 3], lambda x: x > 1) # True
every([1, 2, 3]) # True
every([0, 1, 2]) # False
```
