# Vérifier si certains éléments de liste sont évalués à True

## Problème

Écrivez une fonction `some(lst, fn)` qui prend une liste `lst` et une fonction `fn` en arguments. La fonction devrait renvoyer `True` si la fonction `fn` renvoie `True` pour au moins un élément de la liste `lst`. Si aucun élément de la liste ne satisfait la condition, la fonction devrait renvoyer `False`. Si aucune fonction n'est fournie, la fonction devrait utiliser la fonction identité (qui renvoie l'élément lui-même).

## Exemple

```python
some([0, 1, 2, 0], lambda x: x >= 2 ) # True
some([0, 0, 1, 0]) # True
some(['', 'hello', 'world'], bool) # True
some(['', '', ''], bool) # False
```
