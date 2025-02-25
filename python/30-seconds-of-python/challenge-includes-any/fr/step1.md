# Vérifiez si une valeur quelconque d'une liste est incluse dans une autre liste

## Problème

Écrivez une fonction `includes_any(lst, values)` qui prend deux listes en arguments. La fonction doit vérifier si un élément quelconque de `values` est inclus dans `lst`. Si une valeur est trouvée, la fonction doit renvoyer `True`, sinon, elle doit renvoyer `False`.

Pour résoudre ce problème, vous pouvez utiliser une boucle `for` pour parcourir chaque valeur de `values`. Ensuite, vous pouvez utiliser l'opérateur `in` pour vérifier si la valeur est incluse dans `lst`. Si une valeur est trouvée, renvoyez `True`. Si aucune valeur n'est trouvée, renvoyez `False`.

## Exemple

```python
includes_any([1, 2, 3, 4], [2, 9]) # True
includes_any([1, 2, 3, 4], [8, 9]) # False
```
