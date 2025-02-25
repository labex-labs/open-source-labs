# Función Curry

## Problema

Escribe una función `curry(fn, *args)` que realice la currying de una función `fn` dada. La función debe devolver una nueva función que se comporte como `fn` con los argumentos dados, `args`, aplicados parcialmente.

## Ejemplo

```python
add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30
```
