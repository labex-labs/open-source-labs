# Comprueba si cada elemento de una lista es falso

## Problema

Escribe una función de Python llamada `none(lst, fn = lambda x: x)` que tome una lista `lst` y una función opcional `fn` como argumentos. La función debe devolver `True` si cada elemento de la lista es falso, y `False` en caso contrario. Si se proporciona la función opcional `fn`, se debe utilizar para determinar la verdadera validez de cada elemento de la lista.

Para determinar si un elemento es falso, puedes utilizar las mismas reglas que la función `bool()` de Python. En general, los siguientes valores se consideran falsos:

- `False`
- `None`
- `0` (entero)
- `0.0` (flotante)
- `''` (cadena vacía)
- `[]` (lista vacía)
- `{}` (diccionario vacío)
- `()` (tupla vacía)
- `set()` (conjunto vacío)

Si se proporciona la función opcional `fn`, debe tomar un argumento y devolver un valor booleano. La función se llamará para cada elemento de la lista, y el valor devuelto se utilizará para determinar la verdadera validez del elemento.

## Ejemplo

```python
assert none([0, 1, 2, 0], lambda x: x >= 2 ) == False
assert none([0, 0, 0]) == True
```
