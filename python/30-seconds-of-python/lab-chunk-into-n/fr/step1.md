# Diviser une liste en N morceaux

Écrivez une fonction Python appelée `chunk_into_n(lst, n)` qui prend une liste `lst` et un entier `n` en entrée et renvoie une liste de `n` listes plus petites, chacune contenant un nombre égal d'éléments de la liste d'origine. Si la liste d'origine ne peut pas être divisée en `n` listes plus petites de manière égale, le dernier morceau devrait contenir les éléments restants.

Pour résoudre ce problème, vous pouvez suivre les étapes suivantes :

1. Calculez la taille de chaque morceau en divisant la longueur de la liste d'origine par `n` et arrondissez au supérieur au plus proche entier en utilisant la fonction `math.ceil()`.
2. Créez une nouvelle liste de taille `n` en utilisant les fonctions `list()` et `range()`.
3. Utilisez la fonction `map()` pour mapper chaque élément de la nouvelle liste à un morceau de la liste d'origine de longueur `size`.
4. Retournez la liste des listes plus petites.

Votre fonction devrait avoir la signature suivante :

```python
def chunk_into_n(lst: list, n: int) -> list:
```

```python
from math import ceil

def chunk_into_n(lst, n):
  size = ceil(len(lst) / n)
  return list(
    map(lambda x: lst[x * size:x * size + size],
    list(range(n)))
  )
```

```python
chunk_into_n([1, 2, 3, 4, 5, 6, 7], 4) # [[1, 2], [3, 4], [5, 6], [7]]
```
