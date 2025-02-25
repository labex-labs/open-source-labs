# Desplazar elementos de una lista

Escribe una función `offset(lst, offset)` que tome una lista `lst` y un entero `offset` como argumentos y devuelva una nueva lista con la cantidad especificada de elementos movidos al final de la lista. Si el `offset` es positivo, mueve los primeros `offset` elementos al final de la lista. Si el `offset` es negativo, mueve los últimos `offset` elementos al principio de la lista.

```python
def offset(lst, offset):
  return lst[offset:] + lst[:offset]
```

```python
offset([1, 2, 3, 4, 5], 2) # [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2) # [4, 5, 1, 2, 3]
```
