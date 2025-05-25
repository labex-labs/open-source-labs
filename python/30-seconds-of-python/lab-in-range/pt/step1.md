# Número em um Intervalo

Escreva uma função `in_range(n, start, end = 0)` que recebe três parâmetros:

- `n`: um número para verificar se ele se enquadra no intervalo
- `start`: o início do intervalo
- `end`: o fim do intervalo (opcional, o valor padrão é 0)

A função deve retornar `True` se o número `n` fornecido se enquadra no intervalo especificado e `False` caso contrário. Se o parâmetro `end` não for especificado, o intervalo é considerado de `0` a `start`.

```python
def in_range(n, start, end = 0):
  return start <= n <= end if end >= start else end <= n <= start
```

```python
in_range(3, 2, 5) # True
in_range(3, 4) # True
in_range(2, 3, 5) # False
in_range(3, 2) # False
```
