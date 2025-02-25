# Eliminar elementos de una lista desde la izquierda

## Problema

Escribe una función `drop(a, n=1)` que tome una lista `a` y un entero opcional `n` como argumentos y devuelva una nueva lista con `n` elementos eliminados desde la izquierda de la lista original. Si no se proporciona `n`, la función debe eliminar solo el primer elemento de la lista.

## Ejemplo

```python
drop([1, 2, 3]) # [2, 3]
drop([1, 2, 3], 2) # [3]
drop([1, 2, 3], 42) # []
```
