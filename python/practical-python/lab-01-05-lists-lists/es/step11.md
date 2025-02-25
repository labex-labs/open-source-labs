# Ejercicio 1.23: Ordenamiento

¿Quieres ordenar una lista? Utiliza el método `sort()`. Prueba:

```python
>>> symlist.sort()
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']
>>>
```

¿Quieres ordenar en orden inverso? Prueba esto:

```python
>>> symlist.sort(reverse=True)
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>>
```

Nota: Ordenar una lista modifica su contenido "in-place". Es decir, los elementos de la lista se reorganizan, pero no se crea una nueva lista como resultado.
