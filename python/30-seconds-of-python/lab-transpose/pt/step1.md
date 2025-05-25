# Transposição de Matriz (Transpose Matrix)

Escreva uma função chamada `transpose(lst)` que recebe uma lista bidimensional como argumento e retorna a transposta da lista fornecida.

Siga estes passos para resolver o problema:

- Use `*lst` para obter a lista fornecida como tuplas.
- Use `zip()` em combinação com `list()` para criar a transposta da lista bidimensional fornecida.

```python
def transpose(lst):
  return list(zip(*lst))
```

```python
transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
```
