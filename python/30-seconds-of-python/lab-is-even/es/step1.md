# Comprobar si un número es par

Escribe una función `is_even(num)` que tome un número como argumento y devuelva `True` si el número es par y `False` si el número es impar. Para comprobar si un número es par o impar, puedes usar el operador de módulo (`%`). Si un número es par, no tendrá resto cuando se divida entre 2. Si un número es impar, tendrá un resto de 1 cuando se divida entre 2.

```python
def is_even(num):
  return num % 2 == 0
```

```python
is_even(3) # False
```
