# Similarité de listes

Écrivez une fonction `similarité(a, b)` qui prend deux listes `a` et `b` en arguments et renvoie une nouvelle liste qui contient uniquement les éléments qui existent à la fois dans `a` et `b`.

Pour résoudre ce problème, on peut utiliser la compréhension de liste pour itérer sur les éléments de `a` et vérifier s'ils existent dans `b`. Si un élément existe dans les deux listes, on l'ajoute à une nouvelle liste.

```python
def similarité(a, b):
  return [élément for élément in a if élément in b]
```

```python
similarité([1, 2, 3], [1, 2, 4]) # [1, 2]
```
