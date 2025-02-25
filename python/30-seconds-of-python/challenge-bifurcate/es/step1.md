# Dividir una lista en dos

## Problema

Escribe una función `bifurcate(lst, filter)` que tome una lista `lst` y un filtro `filter` como entrada y devuelva una lista de dos listas. La primera lista debe contener los elementos de `lst` que pasan el filtro, y la segunda lista debe contener los elementos que no.

Para implementar esta función, puedes utilizar una comprensión de lista y la función `zip()`. La función `zip()` toma dos o más listas como entrada y devuelve una lista de tuplas, donde cada tupla contiene los elementos correspondientes de cada lista. Por ejemplo, `zip([1, 2, 3], [4, 5, 6])` devuelve `[(1, 4), (2, 5), (3, 6)]`.

Puedes utilizar esta función para iterar sobre `lst` y `filter` simultáneamente y agregar los elementos a la lista adecuada según pasen o no el filtro.

## Ejemplo

```python
bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# Salida: [['beep', 'boop', 'bar'], ['foo']]
```

En el ejemplo anterior, el filtro es `[True, True, False, True]`. Los primeros dos elementos de `lst` pasan el filtro, por lo que se agregan a la primera lista. El tercer elemento no pasa el filtro, por lo que se agrega a la segunda lista. El cuarto elemento pasa el filtro, por lo que se agrega a la primera lista.
