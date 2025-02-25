# Eliminar elementos de una lista

Escribe una función `take(itr, n=1)` que tome una lista `itr` y un entero `n` como argumentos y devuelva una nueva lista con `n` elementos eliminados del principio de la lista. Si `n` es mayor que la longitud de la lista, devuelve la lista original.

```python
def take(itr, n = 1):
  return itr[:n]
```

```python
take([1, 2, 3], 5) # [1, 2, 3]
take([1, 2, 3], 0) # []
```
