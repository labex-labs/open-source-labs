# Ejercicio 7.5: Clasificación por un campo

Prueba las siguientes declaraciones que clasifican los datos del portafolio alfabéticamente por nombre de acción.

```python
>>> def stock_name(s):
       return s.name

>>> portfolio.sort(key=stock_name)
>>> for s in portfolio:
           print(s)

... inspecciona el resultado...
>>>
```

En esta parte, la función `stock_name()` extrae el nombre de una acción de una sola entrada en la lista `portfolio`. `sort()` utiliza el resultado de esta función para hacer la comparación.
