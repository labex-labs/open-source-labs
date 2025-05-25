# Fatorial

Escreva uma função `factorial(num)` que recebe um inteiro não negativo `num` como argumento e retorna seu fatorial. A função deve usar recursão para calcular o fatorial. Se `num` for menor ou igual a `1`, retorne `1`. Caso contrário, retorne o produto de `num` e o fatorial de `num - 1`. A função deve lançar uma exceção se `num` for um número negativo ou de ponto flutuante.

```python
def factorial(num):
  if not ((num >= 0) and (num % 1 == 0)):
    raise Exception("Number can't be floating point or negative.")
  return 1 if num == 0 else num * factorial(num - 1)
```

```python
factorial(6) # 720
```
