# Dividir una lista en N trozos

Escribe una función de Python llamada `chunk_into_n(lst, n)` que tome una lista `lst` y un entero `n` como entrada y devuelva una lista de `n` listas más pequeñas, cada una de las cuales contiene un número igual de elementos de la lista original. Si la lista original no se puede dividir uniformemente en `n` listas más pequeñas, el último trozo debe contener los elementos restantes.

Para resolver este problema, puedes seguir estos pasos:

1. Calcula el tamaño de cada trozo dividiendo la longitud de la lista original por `n` y redondeando hacia arriba al entero más cercano utilizando la función `math.ceil()`.
2. Crea una nueva lista de tamaño `n` utilizando las funciones `list()` y `range()`.
3. Utiliza la función `map()` para mapear cada elemento de la nueva lista a un trozo de la lista original de longitud `size`.
4. Devuelve la lista de listas más pequeñas.

Tu función debe tener la siguiente firma:

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
