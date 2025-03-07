# Vérifiez si une liste inclut toutes les valeurs

Écrivez une fonction appelée `includes_all(lst, values)` qui prend deux listes en paramètres. La fonction doit vérifier si toutes les valeurs de la liste `values` sont incluses dans la liste `lst`. Si toutes les valeurs sont incluses, la fonction doit renvoyer `True`. Si l'une quelconque des valeurs n'est pas incluse, la fonction doit renvoyer `False`.

Pour résoudre ce problème, vous devriez :

1. Utiliser une boucle `for` pour parcourir chaque valeur de la liste `values`.
2. Vérifier si la valeur actuelle est incluse dans la liste `lst` en utilisant l'opérateur `in`.
3. Si la valeur n'est pas incluse, renvoyer `False`.
4. Si toutes les valeurs sont incluses, renvoyer `True`.

```python
def includes_all(lst, values):
  for v in values:
    if v not in lst:
      return False
  return True
```

```python
includes_all([1, 2, 3, 4], [1, 4]) # True
includes_all([1, 2, 3, 4], [1, 5]) # False
```
