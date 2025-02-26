# Ejercicio 6.13: Expresiones Generadoras

Las expresiones generadoras son una versión generadora de una comprensión de lista. Por ejemplo:

```python
>>> nums = [1, 2, 3, 4, 5]
>>> squares = (x*x for x in nums)
>>> squares
<generator object <genexpr> at 0x109207e60>
>>> for n in squares:
...     print(n)
...
1
4
9
16
25
```

A diferencia de una comprensión de lista, una expresión generadora solo se puede usar una vez. Por lo tanto, si intenta otro bucle for, no obtiene nada:

```python
>>> for n in squares:
...     print(n)
...
>>>
```
