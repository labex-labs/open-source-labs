# Remover Elementos de uma Lista da Direita

Escreva uma função `drop_right(a, n = 1)` que recebe uma lista `a` e um inteiro opcional `n` e retorna uma nova lista com `n` elementos removidos do final direito da lista `a`. Se `n` não for fornecido, a função deve remover apenas o último elemento da lista.

```python
def drop_right(a, n = 1):
  return a[:-n]
```

```python
drop_right([1, 2, 3]) # [1, 2]
drop_right([1, 2, 3], 2) # [1]
drop_right([1, 2, 3], 42) # []
```
