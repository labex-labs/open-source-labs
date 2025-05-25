# Remover Elementos de uma Lista

Escreva uma função `take(itr, n=1)` que recebe uma lista `itr` e um inteiro `n` como argumentos e retorna uma nova lista com `n` elementos removidos do início da lista. Se `n` for maior que o comprimento da lista, retorne a lista original.

```python
def take(itr, n = 1):
  return itr[:n]
```

```python
take([1, 2, 3], 5) # [1, 2, 3]
take([1, 2, 3], 0) # []
```
