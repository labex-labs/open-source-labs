# Encontrar Índice Correspondente

Escreva uma função `find_index(lst, fn)` que recebe uma lista `lst` e uma função de teste `fn` como argumentos. A função deve retornar o índice do primeiro elemento em `lst` para o qual `fn` retorna `True`.

```python
def find_index(lst, fn):
  return next(i for i, x in enumerate(lst) if fn(x))
```

```python
find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0
```
