# União de Listas Baseada em Função

Escreva uma função `union_by(a, b, fn)` que recebe duas listas `a` e `b`, e uma função `fn`. A função deve retornar uma lista que contém cada elemento que existe em qualquer uma das duas listas uma vez, após aplicar a função fornecida a cada elemento de ambas.

Para resolver este problema, você pode seguir estes passos:

1. Crie um `set` aplicando `fn` a cada elemento em `a`.
2. Use uma compreensão de lista em combinação com `fn` em `b` para manter apenas os valores que não estão contidos no conjunto criado anteriormente, `_a`.
3. Finalmente, crie um `set` a partir do resultado anterior e `a` e transforme-o em uma `list`.

A função deve ter os seguintes parâmetros de entrada:

- `a`: uma lista de elementos
- `b`: uma lista de elementos
- `fn`: uma função que recebe um elemento e retorna um valor

A função deve retornar uma lista de elementos.

```python
def union_by(a, b, fn):
  _a = set(map(fn, a))
  return list(set(a + [item for item in b if fn(item) not in _a]))
```

```python
from math import floor

union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]
```
