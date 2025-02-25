# Trier un dictionnaire par clé

## Problème

Écrivez une fonction `sort_dict_by_key(d, reverse=False)` qui prend un dictionnaire `d` et renvoie un nouveau dictionnaire trié par clé. La fonction devrait avoir un paramètre optionnel `reverse` qui par défaut est `False`. Si `reverse` est `True`, le dictionnaire devrait être trié dans l'ordre inverse.

## Exemple

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_key(d) # {'five': 5, 'four': 4, 'one': 1, 'three': 3, 'two': 2}
sort_dict_by_key(d, True) # {'two': 2, 'three': 3, 'one': 1, 'four': 4, 'five': 5}
```
