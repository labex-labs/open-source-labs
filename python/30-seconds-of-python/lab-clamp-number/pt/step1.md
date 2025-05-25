# Fixar Número (_Clamp Number_)

Escreva uma função `clamp_number(num, a, b)` que recebe três parâmetros:

- `num` (inteiro ou _float_): o número a ser fixado
- `a` (inteiro ou _float_): o limite inferior do intervalo
- `b` (inteiro ou _float_): o limite superior do intervalo

A função deve fixar `num` dentro do intervalo inclusivo especificado pelos valores dos limites. Se `num` estiver dentro do intervalo (`a`, `b`), retorne `num`. Caso contrário, retorne o número mais próximo no intervalo.

```python
def clamp_number(num, a, b):
  return max(min(num, max(a, b)), min(a, b))
```

```python
clamp_number(2, 3, 5) # 3
clamp_number(1, -1, -5) # -1
```
