# Listes en dictionnaire

Écrivez une fonction `to_dictionary(keys, values)` qui prend deux listes en entrée et renvoie un dictionnaire où les éléments de la première liste servent de clés et les éléments de la seconde liste servent de valeurs. La fonction devrait utiliser `zip()` en combinaison avec `dict()` pour combiner les valeurs des deux listes en un dictionnaire. La fonction devrait renvoyer `None` si la longueur des deux listes n'est pas égale.

```python
def to_dictionary(keys, values):
  return dict(zip(keys, values))
```

```python
to_dictionary(['a', 'b'], [1, 2]) # { a: 1, b: 2 }
```
