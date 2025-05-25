# Encontrar o Valor Mínimo de uma Lista com Base em uma Função

Escreva uma função chamada `min_by(lst, fn)` que recebe uma lista `lst` e uma função `fn` como argumentos. A função deve mapear cada elemento na lista para um valor usando a função fornecida e, em seguida, retornar o valor mínimo.

```python
def min_by(lst, fn):
  return min(map(fn, lst))
```

```python
min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 2
```
