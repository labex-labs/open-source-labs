# Intersecção de Listas Baseada em Função

Escreva uma função `intersection_by(a, b, fn)` que recebe duas listas `a` e `b`, e uma função `fn`. A função deve retornar uma lista de elementos que existem em ambas as listas, após aplicar a função fornecida a cada elemento de ambas as listas.

### Entrada

- Duas listas `a` e `b` (1 <= len(a), len(b) <= 1000)
- Uma função `fn` que recebe um argumento e retorna um valor

### Saída

- Uma lista de elementos que existem em ambas as listas, após aplicar a função fornecida a cada elemento de ambas as listas.

```python
def intersection_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) in _b]
```

```python
from math import floor

intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]
```
