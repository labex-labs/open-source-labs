# Expresiones generadoras

Una expresión generadora es casi exactamente igual que una comprensión de lista, excepto que no crea una lista. En su lugar, crea un objeto que produce los resultados de forma incremental, generalmente para ser consumidos por iteración. Prueba un ejemplo simple:

```python
>>> nums = [1,2,3,4,5]
>>> squares = (x*x for x in nums)
>>> squares
<generator object <genexpr> at 0x37caa8>
>>> for n in squares:
        print(n)

1
4
9
16
25
>>>
```

Notarás que una expresión generadora solo se puede usar una vez. Observa lo que pasa si haces el bucle `for` nuevamente:

```python
>>> for n in squares:
         print(n)

>>>
```

Puedes obtener los resultados manualmente uno por uno si usas la función `next()`. Prueba esto:

```python
>>> squares = (x*x for x in nums)
>>> next(squares)
1
>>> next(squares)
4
>>> next(squares)
9
>>>
```

Sigue escribiendo `next()` para ver lo que pasa cuando ya no hay más datos.

Si la tarea que estás realizando es más complicada, aún puedes aprovechar los generadores escribiendo una función generadora y usando la declaración `yield` en su lugar. Por ejemplo:

```python
>>> def squares(nums):
        for x in nums:
            yield x*x

>>> for n in squares(nums):
        print(n)

1
4
9
16
25
>>>
```

Volveremos a las funciones generadoras un poco más adelante en el curso. Por ahora, simplemente considera a tales funciones como teniendo la interesante propiedad de suministrar valores a la declaración `for`.
