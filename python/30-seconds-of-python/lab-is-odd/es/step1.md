# Comprobar si un número es impar

Escribe una función llamada `is_odd` que tome un solo entero como argumento y devuelva `True` si el número es impar y `False` si el número es par. Tu función debe realizar los siguientes pasos:

1. Utiliza el operador de módulo (`%`) para comprobar si el número es par o impar.
2. Si el número es impar, devuelve `True`. Si el número es par, devuelve `False`.

```python
def is_odd(num):
  return num % 2!= 0
```

```python
is_odd(3) # True
```
