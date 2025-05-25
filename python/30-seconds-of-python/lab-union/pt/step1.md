# União de Listas (List Union)

Escreva uma função Python chamada `list_union(a, b)` que recebe duas listas como entrada e retorna uma nova lista contendo todos os elementos únicos de ambas as listas. Sua função deve realizar as seguintes etapas:

1.  Combine as duas listas de entrada `a` e `b` em uma única lista.
2.  Remova quaisquer duplicatas da lista combinada.
3.  Retorne a nova lista contendo todos os elementos únicos.

Sua função não deve modificar as listas de entrada `a` e `b`.

```python
def union(a, b):
  return list(set(a + b))
```

```python
union([1, 2, 3], [4, 3, 2]) # [1, 2, 3, 4]
```
