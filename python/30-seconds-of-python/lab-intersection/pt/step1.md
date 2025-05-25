# Interseção de Listas (List Intersection)

Escreva uma função `list_intersection(a, b)` que recebe duas listas `a` e `b` como entrada e retorna uma nova lista contendo apenas os elementos que estão presentes em ambas `a` e `b`. Se não houver elementos comuns, a função deve retornar uma lista vazia.

```python
def intersection(a, b):
  _a, _b = set(a), set(b)
  return list(_a & _b)
```

```python
intersection([1, 2, 3], [4, 3, 2]) # [2, 3]
```
