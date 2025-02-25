# Desafío de invertir un número

## Problema

Escribe una función `reverse_number(n)` que tome un número como argumento y devuelva el inverso de ese número. La función debe cumplir con los siguientes requisitos:

- La función debe invertir el número, independientemente de que sea positivo o negativo.
- La función debe devolver un número de punto flotante si la entrada es un número de punto flotante, y un entero si la entrada es un entero.
- La función no debe utilizar ninguna función integrada que invierta directamente un número (por ejemplo, `reversed()`).
- La función no debe utilizar ninguna función integrada que convierta directamente un número en una cadena (por ejemplo, `str()`).
- La función no debe utilizar ninguna función integrada que convierta directamente una cadena en un número (por ejemplo, `int()` o `float()`).

## Ejemplo

```python
reverse_number(981) # 189
reverse_number(-500) # -5
reverse_number(73.6) # 6.37
reverse_number(-5.23) # -32.5
```
