# Somar Lista Baseado em Função

Escreva uma função `sum_by(lst, fn)` que recebe uma lista `lst` e uma função `fn` como argumentos. A função deve mapear cada elemento da lista para um valor usando a função fornecida e retornar a soma dos valores.

```python
def sum_by(lst, fn):
  return sum(map(fn, lst))
```

```python
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```
