# Trier une liste en fonction d'indexes

Écrivez une fonction `sort_by_indexes(lst, indexes, reverse=False)` qui prend deux listes en arguments et renvoie une nouvelle liste triée en fonction des index de la seconde liste. La fonction devrait avoir les paramètres suivants :

- `lst` : Une liste d'éléments à trier.
- `indexes` : Une liste d'entiers représentant les index souhaités pour trier la `lst`.
- `reverse` : Un paramètre booléen optionnel qui, lorsqu'il est défini sur `True`, trie la liste dans l'ordre inverse.

La fonction devrait renvoyer une nouvelle liste triée en fonction des index de la seconde liste.

```python
def sort_by_indexes(lst, indexes, reverse=False):
  return [val for (_, val) in sorted(zip(indexes, lst), key=lambda x: \
          x[0], reverse=reverse)]
```

```python
a = ['eggs', 'bread', 'oranges', 'jam', 'apples','milk']
b = [3, 2, 6, 4, 1, 5]
sort_by_indexes(a, b) # ['apples', 'bread', 'eggs', 'jam','milk', 'oranges']
sort_by_indexes(a, b, True)
# ['oranges','milk', 'jam', 'eggs', 'bread', 'apples']
```
