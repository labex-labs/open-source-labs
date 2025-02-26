# Ejercicio 6.14: Expresiones Generadoras en Argumentos de Función

A veces, las expresiones generadoras se colocan en los argumentos de funciones. Al principio puede parecer un poco extraño, pero intente este experimento:

```python
>>> nums = [1,2,3,4,5]
>>> sum([x*x for x in nums])    # Una comprensión de lista
55
>>> sum(x*x for x in nums)      # Una expresión generadora
55
>>>
```

En el ejemplo anterior, la segunda versión que utiliza generadores utilizaría significativamente menos memoria si se estuviera manipulando una lista grande.

En su archivo `portfolio.py`, realizó algunos cálculos que implicaban comprensiones de lista. Intente reemplazarlas con expresiones generadoras.
