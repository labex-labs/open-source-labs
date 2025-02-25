# Trier un dictionnaire

Écrivez une fonction appelée `sort_dict_by_value(d, reverse=False)` qui prend un dictionnaire `d` et le trie par ses valeurs. La fonction devrait renvoyer un nouveau dictionnaire avec les mêmes clés que le dictionnaire original, mais avec les valeurs triées par ordre croissant. Si le paramètre `reverse` est défini sur `True`, la fonction devrait trier le dictionnaire par ordre décroissant.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Utilisez `dict.items()` pour obtenir une liste de paires de tuples à partir de `d`.
2. Triez la liste à l'aide d'une fonction lambda et de `sorted()`.
3. Utilisez `dict()` pour convertir la liste triée en un dictionnaire.
4. Utilisez le paramètre `reverse` dans `sorted()` pour trier le dictionnaire dans l'ordre inverse, en fonction du second argument.

**⚠️ ATTENTION** : Les valeurs du dictionnaire doivent être du même type.

```python
def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_value(d) # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
sort_dict_by_value(d, True)
# {'five': 5, 'four': 4, 'three': 3, 'two': 2, 'one': 1}
```
