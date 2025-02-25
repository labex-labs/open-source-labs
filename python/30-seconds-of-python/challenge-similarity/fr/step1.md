# Similarité de listes

## Problème

Écrivez une fonction `similarité(a, b)` qui prend deux listes `a` et `b` en arguments et renvoie une nouvelle liste qui contient uniquement les éléments qui existent dans les deux `a` et `b`.

Pour résoudre ce problème, nous pouvons utiliser la compréhension de liste pour itérer sur les éléments de `a` et vérifier s'ils existent dans `b`. Si un élément existe dans les deux listes, nous l'ajoutons à une nouvelle liste.

## Exemple

```python
similarité([1, 2, 3], [1, 2, 4]) # [1, 2]
```

Dans cet exemple, la fonction `similarité` prend deux listes `[1, 2, 3]` et `[1, 2, 4]` en arguments. La fonction renvoie une nouvelle liste `[1, 2]` qui contient uniquement les éléments qui existent dans les deux listes.
