# Boucles `for` et tuples

Vous pouvez itérer avec plusieurs variables d'itération.

```python
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in points:
    # Boucle avec x = 1, y = 4
    #            x = 10, y = 40
    #            x = 23, y = 14
    #           ...
```

Lorsque vous utilisez plusieurs variables, chaque tuple est _déballé_ en un ensemble de variables d'itération. Le nombre de variables doit correspondre au nombre d'éléments de chaque tuple.
