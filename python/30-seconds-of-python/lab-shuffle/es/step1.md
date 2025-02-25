# Barajar una lista

Escribe una función `shuffle(lst)` que tome una lista como entrada y devuelva una nueva lista con los mismos elementos en un orden aleatorizado. Tu función debe utilizar el algoritmo de Fisher-Yates para barajar los elementos de la lista.

El algoritmo de Fisher-Yates funciona de la siguiente manera:

1. Comienza con el último elemento de la lista.
2. Genera un índice aleatorio entre 0 y el índice actual.
3. Intercambia el elemento en el índice actual con el elemento en el índice aleatorio.
4. Mueve al siguiente elemento de la lista y repite los pasos 2-3 hasta que todos los elementos hayan sido barajados.

Tu función no debe modificar la lista original. En su lugar, debe crear una nueva lista con los elementos barajados.

Puedes suponer que la lista de entrada contendrá al menos un elemento.

```python
from copy import deepcopy
from random import randint

def shuffle(lst):
  temp_lst = deepcopy(lst)
  m = len(temp_lst)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  return temp_lst
```

```python
foo = [1, 2, 3]
shuffle(foo) # [2, 3, 1], foo = [1, 2, 3]
```
