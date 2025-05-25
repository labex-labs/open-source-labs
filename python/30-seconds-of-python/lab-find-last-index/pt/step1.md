# Encontrar o Último Índice Correspondente

Escreva uma função `find_last_index(lst, fn)` que recebe uma lista `lst` e uma função `fn` como argumentos. A função deve retornar o índice do último elemento em `lst` para o qual `fn` retorna `True`. Se nenhum elemento satisfaz a condição, a função deve retornar `-1`.

```python
def find_last_index(lst, fn):
  return len(lst) - 1 - next(i for i, x in enumerate(lst[::-1]) if fn(x))
```

```python
find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 2
```
