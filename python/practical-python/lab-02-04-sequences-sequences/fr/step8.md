# Boucler sur des entiers

Si vous avez besoin de compter, utilisez `range()`.

```python
for i in range(100):
    # i = 0,1,...,99
```

La syntaxe est `range([start,] end [,step])`

```python
for i in range(100):
    # i = 0,1,...,99
for j in range(10,20):
    # j = 10,11,..., 19
for k in range(10,50,2):
    # k = 10,12,...,48
    # Remarquez comment il compte par pas de 2, et non de 1.
```

- La valeur de fin n'est jamais incluse. Elle reflète le comportement des tranches.
- `start` est facultatif. Valeur par défaut : `0`.
- `step` est facultatif. Valeur par défaut : `1`.
- `range()` calcule les valeurs au fur et à mesure. Il ne stocke pas réellement une plage large de nombres.
