# Eliminar elementos de una lista desde el final

Escribe una función `take_right(lst, n=1)` que tome una lista `lst` y un entero opcional `n` como argumentos y devuelva una nueva lista con `n` elementos eliminados del final de la lista. Si no se proporciona `n`, la función debe eliminar solo el último elemento de la lista.

Para resolver este problema, puedes usar la notación de rebanadas para crear una rebanada de la lista con `n` elementos tomados desde el final.

```python
def take_right(itr, n = 1):
  return itr[-n:]
```

```python
take_right([1, 2, 3], 2) # [2, 3]
take_right([1, 2, 3]) # [3]
```
