# Union de listes

Écrivez une fonction Python appelée `list_union(a, b)` qui prend deux listes en entrée et renvoie une nouvelle liste contenant tous les éléments uniques des deux listes. Votre fonction doit effectuer les étapes suivantes :

1. Combiner les deux listes d'entrée `a` et `b` en une seule liste.
2. Enlever tous les doublons de la liste combinée.
3. Retourner la nouvelle liste contenant tous les éléments uniques.

Votre fonction ne doit pas modifier les listes d'entrée `a` et `b`.

```python
def union(a, b):
  return list(set(a + b))
```

```python
union([1, 2, 3], [4, 3, 2]) # [1, 2, 3, 4]
```
