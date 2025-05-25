# Verificar se um Número é Par

Escreva uma função `is_even(num)` que recebe um número como argumento e retorna `True` se o número for par e `False` se o número for ímpar. Para verificar se um número é par ou ímpar, você pode usar o operador de módulo (`%`). Se um número é par, ele não terá resto quando dividido por 2. Se um número é ímpar, ele terá um resto de 1 quando dividido por 2.

```python
def is_even(num):
  return num % 2 == 0
```

```python
is_even(3) # False
```
