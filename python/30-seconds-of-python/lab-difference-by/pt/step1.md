# Diferença de Lista Baseada em Função

Crie uma função chamada `difference_by(a, b, fn)` que recebe três parâmetros:

- `a`: uma lista de elementos
- `b`: uma lista de elementos
- `fn`: uma função que será aplicada a cada elemento em ambas as listas

A função deve retornar uma lista de elementos que estão na lista `a`, mas não na lista `b`, após aplicar a função `fn` fornecida a cada elemento em ambas as listas.

Para resolver este problema, você pode seguir estes passos:

1. Crie um `set`, usando `map()` para aplicar `fn` a cada elemento em `b`.
2. Use uma compreensão de lista em combinação com `fn` em `a` para manter apenas os valores que não estão contidos no conjunto criado anteriormente, `_b`.

```python
def difference_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) not in _b]
```

```python
from math import floor

difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])
# [ { x: 2 } ]
```
