# Initialiser une liste 2D

Écrivez une fonction `initialiser_liste_2d(l, h, val = None)` qui initialise une liste 2D de largeur et de hauteur données avec une valeur. La fonction devrait renvoyer une liste de `h` lignes où chaque ligne est une liste de longueur `l`, initialisée avec `val`. Si `val` n'est pas fournie, la valeur par défaut devrait être `None`.

```python
def initialiser_liste_2d(l, h, val = None):
  return [[val for x in range(l)] for y in range(h)]
```

```python
initialiser_liste_2d(2, 2, 0) # [[0, 0], [0, 0]]
```
