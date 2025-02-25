# Initialiser une liste avec une plage

Écrivez une fonction `initialize_list_with_range(end, start=0, step=1)` qui initialise une liste contenant les nombres dans la plage spécifiée où `start` et `end` sont inclusifs avec leur différence commune `step`.

La fonction devrait renvoyer une liste de la longueur appropriée, remplie avec les valeurs souhaitées dans la plage donnée.

### Entrée

- `end` (entier) - La fin de la plage (inclusive).
- `start` (entier, facultatif) - Le début de la plage (inclusive). La valeur par défaut est 0.
- `step` (entier, facultatif) - La différence commune entre chaque nombre dans la plage. La valeur par défaut est 1.

### Sortie

- Une liste contenant les nombres dans la plage spécifiée.

```python
def initialize_list_with_range(end, start = 0, step = 1):
  return list(range(start, end + 1, step))
```

```python
initialize_list_with_range(5) # [0, 1, 2, 3, 4, 5]
initialize_list_with_range(7, 3) # [3, 4, 5, 6, 7]
initialize_list_with_range(9, 0, 2) # [0, 2, 4, 6, 8]
```
