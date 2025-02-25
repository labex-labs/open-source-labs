# N Elementos Máximos

Escribe una función `max_n(lst, n = 1)` que tome una lista `lst` y un entero opcional `n` como argumentos y devuelva una lista con los `n` elementos máximos de la lista proporcionada. Si no se proporciona `n`, la función debe devolver una lista que contenga el elemento máximo de la lista. Si `n` es mayor o igual que la longitud de la lista, la función debe devolver la lista original ordenada en orden descendente.

Tu tarea es implementar la función `max_n()`.

```python
def max_n(lst, n = 1):
  return sorted(lst, reverse = True)[:n]
```

```python
max_n([1, 2, 3]) # [3]
max_n([1, 2, 3], 2) # [3, 2]
```
