# N Elementos Máximos

Escreva uma função `max_n(lst, n = 1)` que recebe uma lista `lst` e um inteiro opcional `n` como argumentos e retorna uma lista dos `n` elementos máximos da lista fornecida. Se `n` não for fornecido, a função deve retornar uma lista contendo o elemento máximo da lista. Se `n` for maior ou igual ao comprimento da lista, a função deve retornar a lista original ordenada em ordem decrescente.

Sua tarefa é implementar a função `max_n()`.

```python
def max_n(lst, n = 1):
  return sorted(lst, reverse = True)[:n]
```

```python
max_n([1, 2, 3]) # [3]
max_n([1, 2, 3], 2) # [3, 2]
```
