# Conjunto das Partes (Powerset)

Escreva uma função Python chamada `powerset(iterable)` que recebe um iterável como argumento e retorna o conjunto das partes (powerset) do iterável. A função deve seguir estes passos:

1.  Converter o valor dado em uma lista.
2.  Usar `range()` e `itertools.combinations()` para criar um gerador que retorna todos os subconjuntos.
3.  Usar `itertools.chain.from_iterable()` e `list()` para consumir o gerador e retornar uma lista.

```python
from itertools import chain, combinations

def powerset(iterable):
  s = list(iterable)
  return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
```

```python
powerset([1, 2]) # [(), (1,), (2,), (1, 2)]
```
