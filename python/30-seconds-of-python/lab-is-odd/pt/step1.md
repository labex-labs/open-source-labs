# Verificar se um Número é Ímpar

Escreva uma função chamada `is_odd` que recebe um único inteiro como argumento e retorna `True` se o número for ímpar e `False` se o número for par. Sua função deve realizar as seguintes etapas:

1.  Use o operador de módulo (`%`) para verificar se o número é par ou ímpar.
2.  Se o número for ímpar, retorne `True`. Se o número for par, retorne `False`.

```python
def is_odd(num):
  return num % 2 != 0
```

```python
is_odd(3) # True
```
