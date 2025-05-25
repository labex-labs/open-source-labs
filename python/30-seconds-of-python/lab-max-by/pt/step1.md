# Encontrar o Valor Máximo da Lista com Base em uma Função

Escreva uma função `max_by(lst, fn)` que recebe uma lista `lst` e uma função `fn` como argumentos. A função deve mapear cada elemento em `lst` para um valor usando a função fornecida `fn` e, em seguida, retornar o valor máximo.

```python
def max_by(lst, fn):
  return max(map(fn, lst))
```

```python
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
```
