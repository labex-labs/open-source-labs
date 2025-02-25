# Dividir una lista en dos

Escribe una función `bifurcate(lst, filter)` que tome una lista `lst` y un filtro `filter` como entrada y devuelva una lista de dos listas. La primera lista debe contener los elementos de `lst` que pasan el filtro, y la segunda lista debe contener los elementos que no.

Para implementar esta función, puedes utilizar una comprensión de lista y la función `zip()`. La función `zip()` toma dos o más listas como entrada y devuelve una lista de tuplas, donde cada tupla contiene los elementos correspondientes de cada lista. Por ejemplo, `zip([1, 2, 3], [4, 5, 6])` devuelve `[(1, 4), (2, 5), (3, 6)]`.

Puedes utilizar esta función para iterar sobre `lst` y `filter` simultáneamente y agregar los elementos a la lista adecuada según pasen o no el filtro.

```python
def bifurcate(lst, filter):
  return [
    [x for x, flag in zip(lst, filter) if flag],
    [x for x, flag in zip(lst, filter) if not flag]
  ]
```

```python
bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```
