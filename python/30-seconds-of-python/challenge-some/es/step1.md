# Comprueba si algunos elementos de una lista son verdaderos

## Problema

Escribe una función `some(lst, fn)` que tome una lista `lst` y una función `fn` como argumentos. La función debe devolver `True` si la función `fn` devuelve `True` para al menos un elemento de la lista `lst`. Si ningún elemento de la lista satisface la condición, la función debe devolver `False`. Si no se proporciona ninguna función, la función debe usar la función identidad (que devuelve el elemento mismo).

## Ejemplo

```python
some([0, 1, 2, 0], lambda x: x >= 2 ) # True
some([0, 0, 1, 0]) # True
some(['', 'hello', 'world'], bool) # True
some(['', '', ''], bool) # False
```
