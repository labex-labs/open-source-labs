# Tous les index de la valeur

Écrivez une fonction Python appelée `index_of_all(lst, value)` qui prend une liste `lst` et une valeur `value` en arguments et renvoie une liste d'index de toutes les occurrences de `value` dans `lst`.

Pour résoudre ce problème, vous pouvez utiliser `enumerate()` et une compréhension de liste pour vérifier chaque élément pour l'égalité avec `value` et ajouter `i` au résultat.

```python
def index_of_all(lst, value):
  return [i for i, x in enumerate(lst) if x == value]
```

```python
index_of_all([1, 2, 1, 4, 5, 1], 1) # [0, 2, 5]
index_of_all([1, 2, 3, 4], 6) # []
```
