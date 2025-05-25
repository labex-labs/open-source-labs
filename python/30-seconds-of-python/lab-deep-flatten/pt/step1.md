# Deep Flatten List (Achatamento Profundo de Lista)

Escreva uma função `deep_flatten(lst)` que recebe uma lista `lst` como argumento e retorna uma nova lista que é a versão com _deep flatten_ (achatamento profundo) de `lst`. A função deve usar recursão e a função `isinstance()` com `collections.abc.Iterable` para verificar se um elemento é iterável. Se um elemento for iterável, a função deve aplicar `deep_flatten()` recursivamente a esse elemento. Caso contrário, a função deve retornar uma lista contendo apenas esse elemento.

```python
from collections.abc import Iterable

def deep_flatten(lst):
  return ([a for i in lst for a in
          deep_flatten(i)] if isinstance(lst, Iterable) else [lst])
```

```python
deep_flatten([1, [2], [[3], 4], 5]) # [1, 2, 3, 4, 5]
```
