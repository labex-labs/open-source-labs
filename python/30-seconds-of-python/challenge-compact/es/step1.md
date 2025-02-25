# Lista Compacta

## Problema

Escribe una función `compact(lst)` que tome una lista como argumento y devuelva una nueva lista sin todos los valores falsos. Los valores falsos incluyen `False`, `None`, `0` y `""`.

Para resolver este problema, puedes usar la función `filter()` para filtrar los valores falsos de la lista.

## Ejemplo

```python
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```
