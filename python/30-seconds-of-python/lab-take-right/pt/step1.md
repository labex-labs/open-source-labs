# Remover Elementos do Final da Lista

Escreva uma função `take_right(lst, n=1)` que recebe uma lista `lst` e um inteiro opcional `n` como argumentos e retorna uma nova lista com `n` elementos removidos do final da lista. Se `n` não for fornecido, a função deve remover apenas o último elemento da lista.

Para resolver este problema, você pode usar a notação de fatiamento (slice notation) para criar uma fatia da lista com `n` elementos tomados do final.

```python
def take_right(itr, n = 1):
  return itr[-n:]
```

```python
take_right([1, 2, 3], 2) # [2, 3]
take_right([1, 2, 3]) # [3]
```
