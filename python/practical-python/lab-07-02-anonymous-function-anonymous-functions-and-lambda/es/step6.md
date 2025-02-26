# Ejercicio 7.6: Clasificación por un campo con lambda

Prueba a clasificar el portafolio según el número de acciones utilizando una expresión `lambda`:

```python
>>> portfolio.sort(key=lambda s: s.shares)
>>> for s in portfolio:
        print(s)

... inspecciona el resultado...
>>>
```

Prueba a clasificar el portafolio según el precio de cada acción

```python
>>> portfolio.sort(key=lambda s: s.price)
>>> for s in portfolio:
        print(s)

... inspecciona el resultado...
>>>
```

Nota: `lambda` es un atajo útil porque te permite definir una función de procesamiento especial directamente en la llamada a `sort()` en lugar de tener que definir una función separada primero.
