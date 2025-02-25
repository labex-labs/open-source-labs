# Ejercicio 1.17: cadenas f

A veces quieres crear una cadena y embeber los valores de variables en ella.

Para hacer eso, utiliza una cadena f. Por ejemplo:

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{shares} acciones de {name} a ${price:0.2f}'
'100 acciones de IBM a $91.10'
>>>
```

Modifica el programa `mortgage.py` del Ejercicio 1.10 para crear su salida utilizando cadenas f. Intenta hacerlo de modo que la salida esté bien alineada.
