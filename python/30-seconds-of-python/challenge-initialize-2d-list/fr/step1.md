# Initialiser une liste 2D

## Problème

Écrivez une fonction `initialiser_liste_2d(l, h, val=None)` qui initialise une liste 2D de largeur et de hauteur données avec une valeur donnée. La fonction devrait renvoyer une liste de `h` lignes où chaque ligne est une liste de longueur `l`, initialisée avec `val`. Si `val` n'est pas fournie, la valeur par défaut devrait être `None`.

## Exemple

```python
initialiser_liste_2d(2, 2, 0) # [[0, 0], [0, 0]]
initialiser_liste_2d(3, 3, "x") # [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
initialiser_liste_2d(2, 3) # [[None, None], [None, None], [None, None]]
```
