# Listas para Dicionário

Escreva uma função `to_dictionary(keys, values)` que recebe duas listas como entrada e retorna um dicionário onde os elementos da primeira lista servem como as chaves e os elementos da segunda lista servem como os valores. A função deve usar `zip()` em combinação com `dict()` para combinar os valores das duas listas em um dicionário. A função deve retornar `None` se o comprimento das duas listas não for igual.

```python
def to_dictionary(keys, values):
  return dict(zip(keys, values))
```

```python
to_dictionary(['a', 'b'], [1, 2]) # { a: 1, b: 2 }
```
