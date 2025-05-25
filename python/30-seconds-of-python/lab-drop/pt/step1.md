# Remover Elementos de uma Lista da Esquerda

Escreva uma função `drop(a, n=1)` que recebe uma lista `a` e um inteiro opcional `n` como argumentos e retorna uma nova lista com `n` elementos removidos da esquerda da lista original. Se `n` não for fornecido, a função deve remover apenas o primeiro elemento da lista.

```python
def drop(a, n = 1):
  return a[n:]
```

```python
drop([1, 2, 3]) # [2, 3]
drop([1, 2, 3], 2) # [3]
drop([1, 2, 3], 42) # []
```
