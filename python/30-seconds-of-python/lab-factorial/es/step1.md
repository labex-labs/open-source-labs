# Factorial

Escribe una función `factorial(num)` que tome un número entero no negativo `num` como argumento y devuelva su factorial. La función debe utilizar recursión para calcular el factorial. Si `num` es menor o igual a `1`, devuelve `1`. En caso contrario, devuelve el producto de `num` y el factorial de `num - 1`. La función debe lanzar una excepción si `num` es un número negativo o de punto flotante.

```python
def factorial(num):
  if not ((num >= 0) and (num % 1 == 0)):
    raise Exception("Number can't be floating point or negative.")
  return 1 if num == 0 else num * factorial(num - 1)
```

```python
factorial(6) # 720
```
