# Ejercicio 2.19: Comprensiones de lista

Prueba algunas comprensiones de lista simples solo para familiarizarte con la sintaxis.

```python
>>> nums = [1,2,3,4]
>>> squares = [ x * x for x in nums ]
>>> squares
[1, 4, 9, 16]
>>> twice = [ 2 * x for x in nums if x > 2 ]
>>> twice
[6, 8]
>>>
```

Observa cómo las comprensiones de lista están creando una nueva lista con los datos adecuadamente transformados o filtrados.
