# Número é divisível

Escreva uma função `is_divisible(dividendo, divisor)` que recebe dois inteiros como argumentos e retorna `True` se o `dividendo` é divisível pelo `divisor`, e `False` caso contrário.

```python
def is_divisible(dividend, divisor):
  return dividend % divisor == 0
```

```python
is_divisible(6, 3) # True
```
